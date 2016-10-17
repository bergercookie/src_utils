# Mon May 26 07:32:21 EEST 2014, nickkouk

""" 
This is the pump model.

It is designed to implement all the basic controls of the pump independent of
the way the user tries to interact with the pump (GUI, CLI, etc).
There should be 2 ways for the pump to communicate:
    Serial Communication
    Pipe Communication for testing purposes

"""

from __future__ import division
import serial
import threading


class Pump():
    def __init__(self, addr, com = 'serial'):

        # Connection settings
        self.port_name = 'loop://'
        self.baud = 9600
        self.byte_size = 8
        self.par = 'N' 
        self.stopb = 1
        self.timeout_time = 0 

        self.addr = '/%s' %addr
        self.term = 'R\r'
        self.ser = serial.serial_for_url(self.port_name,\
                timeout = self.timeout_time) #testings purposes
        self.com = com

        # Control Related properties
        self.history = []
        self.refresh = True 
        self.interval = 2

        # Use thread locks to ensure threading synchronisation
        self.lock = threading.Lock()

        # Dictionary for holding the pump properties
        self.status = {"absolute_pos": '',\
                "top_vel": '', "cutoff_vel": '',\
                "actual_pos": '', \
                "starting_vel": '',\
                "backlash_steps": '',\
                "fluid_sensor": '',\
                "buffer_status": '',\
                "version": '',\
                "checksum": ''}


        # Hold local properties
        self.own_status = {"plung_pos_mine": 0,\
                "valve_pos": '0',\
                "plung_speed": 10,\
                "steps_tot": 3000,\
                "syringe_size": 50}

        self.initialize_pump()
        self.update_values()

    # Sending Mechanism
    def send_Command(self, command, bits_to_read = 10):
        """
        Basic function for serial communication with the pump.

        Every other method that wants to send a command to the pump
        via the serial interface and then receive its outcome must use 
        the send_Command method to avoid threading miscommunication and ensure
        robustness

        Includes locking mechanism to avoid more than one thread from 
        accessing the serial line

        2 Modes:
        --- Test Mode (Default): Initialize a pump and print every command 
        in the std output instead of a read serial port
        --- Serial: Real deal, communicate with the pump

        Things to Notice:
        --- The plunger should ALWAYS execute a ser.read after a ser.write
        because if opposite the next ser.read is fetching the previous' 
        ser.write answer

        """

        self.lock.acquire()
        try:
            if self.com == 'serial':
                full_command = self.addr + command + self.term
                self.ser.write(full_command)
                return_stat = self.ser.read(bits_to_read)
                self.history.append(full_command)
            elif self.com == 'test':
                full_command = self.addr + command + self.term
                print (full_command)
                self.history.append(full_command)
                return_stat = full_command
        finally:
            self.lock.release()
            return return_stat

    # Initialization Phase
    def initialize_pump(self):
        if not self.ser.isOpen():
            self.ser.open()

        commands = ['Z', 'S10', ]
        for command in commands:
            self.send_Command(command)

    # New serial connection
    def accept_new(self, port_name):
        if port_name != 'loop://':
            self.port_name = port_name
            self.ser = serial.Serial(port = self.port_name,\
                    baudrate = self.baud,\
                    timeout = self.timeout_time )
        else:
            self.ser = serial.serial_for_url(self.port_name,\
                    timeout = self.timeout_time) #testings purposes

        self.history = [ ]
        self.initialize_pump()
        # Empty the history as well
    

    # Valve Functions
    def output_Valve(self):
        if self.own_status["valve_pos"] != 'O':
            self.send_Command('O', 8)
            self.own_status["valve_pos"] = 'O'

    def input_Valve(self):
        if self.own_status["valve_pos"] != 'I':
            self.send_Command('I', 8)
            self.own_status["valve_pos"] = 'I'

    def bypass_Valve(self):
        if self.own_status["valve_pos"] != 'B':
            self.send_Command('B', 8)
            self.own_status["valve_pos"] = 'B'

    # Plunger Functions
    def setPlungerSpeed(self, speed):
        if self.own_status["plung_speed"] != speed:
            self.send_Command('S' + "%s" %speed, 0)
            self.own_status["plung_speed"] = speed

    def volume_command(self, vol, direction):
        """
        This is the volume command.

        The volume_command function first decides if it can 
        deliver the needed volume, 
        then if the volume given is a valid one,
        calls the move_plunger method with the needed arguments
        to deliver the volume.

        """
        if not vol.isdigit():
            return (False, "Please enter a numerical value")

        vol = float(vol)
        # TODO Should the steps be just integers or can I also pass real??
        steps = int(self.own_status["steps_tot"] / \
                self.own_status["syringe_size"] * vol)

        if direction == 'D':
            if self.own_status["plung_pos_mine"] - steps < 0:
                return (False, "Not a valid value")
            else:
                self.own_status["plung_pos_mine"] -= steps
                answer = self.send_Command(direction + "%s" %steps)
                return (True, answer)

        elif direction == 'P':
            if self.own_status["plung_pos_mine"] +\
                    steps > self.own_status["steps_tot"]:
                        return (False, "Not a valid value")
            else: 
                self.own_status["plung_pos_mine"] += steps
                answer = self.send_Command(direction + "%s" %steps)
                return (True, answer)

    def boundary_plunger_action(self, action):
        if action == 'push':
            self.send_Command('A0')
        else:
            self.send_Command('A3000')

    def update_values(self):
        """
        The purpose of this function is to constantly update the settings 
        related to the pump, should be run by a thread periodically
        """

        # reading info mechanism
        self.status["absolute_pos"] = self.send_Command('?')
        self.status["actual_pos"] = self.send_Command('?4')
        self.status["starting_vel"] = self.send_Command('?1')
        self.status["top_vel"] = self.send_Command('?2')
        self.status["cutoff_vel"] = self.send_Command('?3')
        self.status["backlash_steps"] = self.send_Command('?12')
        self.status["fluid_sensor"] = self.send_Command('?22')
        self.status["buffer_status"] = self.send_Command('?F')
        self.status["version"] = self.send_Command('?&')
        self.status["checksum"] = self.send_Command('?#')

        # Update own variables as well
        #self.own_status["plung_pos_mine"] = self.status["actual_pos"]

        if self.refresh == True:
            self.update_timer = threading.Timer(self.interval, self.update_values)
            self.update_timer.start()

    def cancel_timer(self):
        """
        The purpose of the cancel_timer is to cancel the status refreshing.
        Can be used by the user to manually update the pump status 

        """
        self.update_timer.cancel()
        self.refresh = False
        print "TIMER closed"

    def setTimer_interval(self): 
        if self.refresh == True:
            self.update_timer = threading.Timer(self.interval, self.update_values)
            self.update_timer.start()
        print "ok! iterval is {}".format(self.interval)
