#!/usr/bin/env bash
# Fri Aug 26 16:50:13 EEST 2016, Nikos Koukis
# Initialize an empty directory and populate it with two dummy files

bash_scripts="$HOME/src/bash/"
cd $bash_scripts

if ! [[ -d a_dir ]]; then
    mkdir a_dir
fi

for f in {file_a,file_b}; do
    f_name=a_dir/$f
    touch $f_name
    echo $( date ) >> $f_name
    printf "%s\n" kalimera >> $f_name
done

