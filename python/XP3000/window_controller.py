#!/usr/bin/env python
# Mon May 26 23:48:35 EEST 2014, nickkouk
"""
Python Implementation for the Cavro XP3000 GUI.

The GUI is designed with regards to the MVC (Model View Controller)
Ui architectural pattern. Inside this module the View - Controller behaviors
are implemented while the Model behavior is implemented in the imported module:
    pump_model.py

"""


# proper division for python 2.7
from __future__ import division

# Usual importing stuff for PySide
from PySide.QtGui import *
from PySide.QtCore import *

# Module imports
import sys
import os
from classes_used import HistoryDialog,\
        ReportsDialog, \
        NewDevDialog

# Qt-Designer compiled python code
import python_gui
import python_settings
import history_settings
import device_configuration

import pump_model

class MainWindow(QMainWindow, python_gui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.__appname__ = "XP3000 Interface"
        self.setWindowTitle(self.__appname__)

        # Initialize a pump instance
        self.pump = pump_model.Pump(1, 'serial')

        # MainWindow related parameters
        self.quick_action = 'push'
        self.editors_open = 1
        self.lcdNumber.display(10)

        self.tabWidget.setTabText(0, 'Controls')
        self.tabWidget.setTabText(1, 'Editor - {}'.format(self.editors_open))

        # Connecting signals to functions
        self.connect(self.output_btn,\
                SIGNAL("clicked()"),\
                self.pump.output_Valve)
        self.connect(self.input_btn,\
                SIGNAL("clicked()"),\
                self.pump.input_Valve)
        self.connect(self.bypass_btn,\
                SIGNAL("clicked()"),\
                self.pump.bypass_Valve)

        self.connect(self.speed_slider,\
                SIGNAL("sliderReleased()"),\
                self.speed_control)
        self.connect(self.speed_slider,\
                SIGNAL("valueChanged(int)"),\
                self.lcd_display)

        self.connect(self.volume_prompt,\
                SIGNAL("returnPressed()"),\
                self.volume_control)
        self.connect(self.quick_combobox,\
                SIGNAL("currentIndexChanged(int)"),\
                self.push_pull)
        self.connect(self.address_combobox,\
                SIGNAL("currentIndexChanged(int)"),\
                self.set_address)
        self.connect(self.make_it_so,\
                SIGNAL("clicked()"),\
                self.make_it_so_function)
        self.connect(self, SIGNAL("quit()"), self.pump.cancel_timer)

        self.connect(self.actionReports,\
                SIGNAL("triggered()"),\
                self.reports_window_open)
        self.connect(self.actionHistory,\
                SIGNAL("triggered()"),\
                self.history_window_open)
        self.connect(self.actionNew_Device,\
                SIGNAL("triggered()"),\
                        self.newDev)

        # Editor related action buttons
        #self.connect(self.actionSave,\
                #SIGNAL("triggered()"),\
                #self.save_btn)
        #self.connect(self.actionSaveAs,\
                #SIGNAL("triggered()"),\
                #self.saveAs_btn)
        #self.connect(self.actionOpen,\
                #SIGNAL("triggered()"),\
                #self.open_btn)
        self.connect(self.actionClose,\
                SIGNAL("triggered()"),\
                self.close_btn)
        self.connect(self,\
                SIGNAL("aboutToQuit()"),\
                self.close_btn)
   
    # Basic Window Actions
    def close_btn(self):
        """ 
        Quits the application

        Also closes all the file descriptors that remain open,
        and cancel all the open timers
        """
        self.pump.cancel_timer()
        self.close()

    # Functions for either fulling or emptying the whole syringe
    def push_pull(self):
        if self.quick_combobox.currentIndex() == 0:
            self.quick_action = 'push'
        else:
            self.quick_action = 'pull'
    def make_it_so_function(self):
        self.pump.boundary_plunger_action(self.quick_action)

    # Opening Dialogs
    def history_window_open(self):
        """ Opens a HistoryDialog Instance"""

        self.history_window = HistoryDialog(self.pump)
        self.history_window.show()
        self.history_window.raise_()
        self.history_window.refresh_Btn.click()

    def reports_window_open(self):
        """ Opens a ReportsDialog Instance"""

        self.reports_window = ReportsDialog(self.pump)

        self.connect(self.reports_window.noRefresh,\
                SIGNAL("clicked()"),\
                self.reports_window.tick_refresh)

        self.connect(self.reports_window,\
                SIGNAL("rejected()"),\
                self.pump.cancel_timer)

        self.reports_window.refresh()
        self.reports_window.show()
        self.reports_window.raise_()
   
    # Device Configuration
    def newDev(self):
        QMessageBox.information(self, "New Pump Configuration", "Select the device name")

        self.dev_window = NewDevDialog(self.pump)
        self.dev_window.show()
        self.dev_window.exec_()

        self.connect(self.dev_window,\
                SIGNAL("ccepted()"),\
            self.dev_window.connect_with_port())

    def set_address(self):
        self.pump.addr = '/%s' %self.address_combobox.currentText()
        print "kalimera PUMP ADDRESS: {}".format(self.pump.addr)

       
    # Plunger speed
    def speed_control(self):
        """function for calling the pump.setPlungerSpeed function"""
        speed = self.speed_slider.value()
        self.pump.setPlungerSpeed(speed)
    def lcd_display(self):
        speed = self.speed_slider.value()
        self.lcdNumber.display(speed)

    def volume_control(self):
        """function for calling the pump.volume_command method."""

        volume = self.volume_prompt.text()

        if self.PushBtn.isChecked():
            direction = "D"
        elif self.PullBtn.isChecked():
            direction = "P"
        else:
            raise Exception("Something is wrong in the volume_control function")

        #print "volume: {0}\n volume_type: {1}\n direction: {2}: ".format(volume, type(volume), direction)

        (done, answer) = self.pump.volume_command(volume, direction)
        #print "done: {0}\n answer: {1}".format(done, answer)

        if not done:
            QMessageBox.warning(self, self.__appname__, answer)

        self.volume_prompt.selectAll()
        #if done:
            #print "plunger own status position %s" % self.pump.own_status["plung_pos_mine"]
            #print "answer: %s" % answer


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window= MainWindow()
    window.show()
    app.exec_() # Event-loop of the application
