#!/usr/bin/env python

"""
*** DOCUMENTATION ***
This code is used primarily for troubleshooting the connection with the pump
using the pyserial module
"""

# Imports first

import serial
import io
import time

class XP3000_pump():
    
    # parameters
    baud = 9600
    data_bits = 8
    parity = None
    stop_bits = 1

    def __init__(self, port = '/dev/tty.usbserial-FTDWBH0Y'):
        self.port = port
        self.isOpen = False

    ## Open and initize the serial port ##
    def start(self):
        if not self.isOpen :
            self.ser = serial.Serial()
            self.ser.setBaudrate(9600)
            self.ser.setByteSize(bytesize = 8)
            self.ser.setParity('N')
            self.ser.timeout = 2
            self.ser.stopbits = self.stop_bits
            self.ser.port = self.port

            self.ser.open()
            print( "Opened port." )
            self.sio = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser )) # TextWrapper
            self.isOpen = True
            return

    ## Write ##
    def w( self, command ):
        self.start()
        time.sleep( 0.1 )
        self.sio.write( command + str( "\n" ) )
        self.sio.flush()
        print( "{0:10}{1}".format( "Sent:", command ) )
        return

    ## Read ##
    def read( self, byte ):
        self.start()
        read = self.ser.read( byte )
        print( "{0:10}{1}".format( "Read:", read ) )
        return read


    ## Close the serial port ##
    def close( self ):
        self.ser.close()
        self.isOpen = False
        print( "Closed port." )
        return
