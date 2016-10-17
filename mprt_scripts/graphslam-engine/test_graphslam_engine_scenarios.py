#!/usr/bin/env python

"""
# Mon Oct 17 16:52:23 EEST 2016, Nikos Koukis

Script is used to verify that all the different combinations of NRDs, ERD, GSOs
and datasets do not (at least do not produce any errors).

This can be handy to make sure that the changes introduced do not brake any
possible argument combinations.

"""


import colorama
from colorama import Fore, Style
colorama.init()

import os
import subprocess
import time
from supplementary.custom_exceptions import MRPTExecutableNotFoundError
import shutil


def ePrint(msg=None):
    """Wrapper for the error messages."""
    color_opts = Fore.RED + Style.BRIGHT
    prompt = color_opts + "[ERROR]"
    do_print(prompt, msg)


def iPrint(msg=None):
    """Wrapper for the information messages."""
    color_opts = Fore.WHITE + Style.BRIGHT
    prompt = color_opts + "[INFO]"
    do_print(prompt, msg)


def tPrint(msg=None):
    """Wrapper for the test announcing messages."""
    color_opts = Fore.YELLOW + Style.BRIGHT
    prompt = color_opts + "[TEST]"
    do_print(prompt, msg)


def sPrint(msg=None):
    """Wrapper for the success messages."""
    color_opts = Fore.GREEN + Style.BRIGHT
    prompt = color_opts + "[OK]"
    do_print(prompt, msg)


def do_print(prompt, msg):
    """Low level print wrapper for displaying progress messages to the user."""
    print(prompt + " " + msg)
    print(Style.RESET_ALL)


def main():
    node_regs = [
        "CFixedIntervalsNRD",
        "CICPCriteriaNRD"
    ]
    edge_regs = [
        "CICPCriteriaERD",
        "CLoopCloserERD"
    ]
    optimizers = ["CLevMarqGSO"]

    datasets_dir = os.environ['dataset'] or os.curdir()
    datasets_dir += os.sep
    dataset_files = ["action_observations_map_short", "observation_only_short"]
    datasets = [datasets_dir + os.sep + d + os.sep for d in dataset_files]

    config_file = "".join([
        "{home}".format(home=os.environ["HOME"]), os.sep,
        "sharedWros/codes/various/mrpt/share/mrpt/config_files/",
        "graphslam-engine/odometry_2DRangeScans.ini"])

    visuals = [True, False]

    combs = [[i, j, k, l, m]
             for i in node_regs
             for j in edge_regs
             for k in optimizers
             for l in datasets
             for m in visuals
             ]
    total_combs = len(combs)


    # find the graphslam-engine executable
    bash_mrpt_var = "MRPT_DIR"

    if bash_mrpt_var in os.environ:
        mrpt_path = os.environ[bash_mrpt_var]
        app_path = "".join([mrpt_path,
                            os.sep, "bin", os.sep,
                            "graphslam-engine"])
    elif subprocess.call(["which", "graphslam-engine"]): # search for it in the user path
        app_path = "graphslam-engine" # already in path
    else: # can't be found - inform user
        raise MRPTExecutableNotFoundError("graphslam-engine")

    errors_num = 0

    # take all the possible combinations and execute graphSLAM
    for comb_i, curr_comb in enumerate(combs):
        #
        # Announce operation
        #
        intro_msg = "# {}/{}".format(comb_i+1, total_combs)
        tPrint(intro_msg)
        node = curr_comb[0]
        edge = curr_comb[1]
        opt = curr_comb[2]
        dataset = curr_comb[3]
        disable_visuals = curr_comb[4] is False

        current_run_input = ""
        current_run_input += "\tNode Registration Decider: {}\n".format(node)
        current_run_input += "\tEdge Registration Decider: {}\n".format(edge)
        current_run_input += "\tGraphSLAM Optimizer      : {}\n".format(opt)
        current_run_input += "\tDataset                  : {}\n".format(
            dataset)
        current_run_input += "\t.ini Configuration File  : {}\n".format(
            config_file)
        current_run_input += "\tDisable visuals          : {}\n".format(
            disable_visuals)
        print(current_run_input)

        #
        # Execute it
        #
        redirect_null = True
        command_parts = [app_path]
        command_parts.extend(["--node-reg", node])
        command_parts.extend(["--edge-reg", edge])
        command_parts.extend(["--optimizer", opt])
        command_parts.extend(["--ini-file", config_file])
        command_parts.extend(["--rawlog", dataset + "basic.rawlog"])
        command_parts.extend(["--ground-truth", dataset + "basic.rawlog.GT.txt"])
        if disable_visuals:
            command_parts.extend(["--disable-visuals"])

        if redirect_null:
            with open(os.devnull, 'w') as fp:
                result = subprocess.Popen(command_parts, stdout=fp).wait()
        else:
            result = subprocess.Popen(command_parts).wait()

        #
        # Announce results
        #
        output_dir_name_init = "graphslam_results"
        dir_exists = os.path.isdir(output_dir_name_init)
        if result == 0:
            sPrint(intro_msg)
            if dir_exists:
                print("Removing the graphslam_results directory")
                shutil.rmtree(output_dir_name_init)
        else:
            errors_num += 1
            code = "Error code: {r}".format(r=result)

            # is there a graphslam_results directory generated?
            if dir_exists:
                # If directory was created, rename it and add a new file in it
                # with the statistics of the current run

                # date string
                date_string = "Automatically generated file - {}".format(
                    time.strftime("%c"))
                date_string.replace(":", "_")
                date_string.replace(" ", "_")

                # new file
                with open(output_dir_name_init + os.sep + "test_info", "w") as f:
                    f.writelines([i + os.linesep for i in [date_string,
                                                           "=" * 60,
                                                           current_run_input]])

                # moving results file
                output_dir_name_moved = "{d}_graphslam_results_test_{i}_of_{t}".format(
                    d=date_string,
                    i=comb_i+1,
                    t=total_combs)
                os.rename(output_dir_name_init, output_dir_name_moved)
                logdir = "For more info on this see directory \"{d}\"".format(
                    d=output_dir_name_moved)
            else:
                logdir = "Results directory was not generated."

            ePrint("\t\n".join([intro_msg, code, logdir]))

    # total report
    iPrint("Summary:")
    if errors_num == 0:
        print("No execution errors were reported... {col}OK".format(
            col=Fore.RED))
    else:
        print("Failed executions: {}/{}... {col}ERROR".format(
            errors_num,
            total_combs,
            col=Fore.RED))



if __name__ == "__main__":
    main()
