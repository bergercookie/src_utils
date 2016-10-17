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

# Qt-Designer compiled python code
import python_gui
import python_settings

from pump_model import Pump

class MainWindow(QMainWindow, python_gui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.__appname__ = "XP3000 Interface"
        self.setWindowTitle(self.__appname__)

        # Initialize a pump instance
        self.pump = pump_model.Pump(1, 'serial')

       # Threading for non-blocking behavior
        #self.updateThread = updateThread(self)
        #self.updateThread.start()

        # Connecting signals to functions
        self.connect(self.output_btn, SIGNAL("clicked()"), self.pump.output_Valve)
        self.connect(self.input_btn, SIGNAL("clicked()"), self.pump.input_Valve)
        self.connect(self.bypass_btn, SIGNAL("clicked()"), self.pump.bypass_Valve)

        self.connect(self.speed_slider, SIGNAL("sliderReleased()"), self.speed_control)
        self.connect(self.speed_spinbox, SIGNAL("editingFinished()"), self.speed_control)
        self.connect(self.volume_prompt, SIGNAL("returnPressed()"), self.volume_control)

        #self.connect(self.actionReports, SIGNAL("triggered()"), self.reports_window)
        #self.connect(self.actionNew_Device, SIGNAL("triggered()"), self.newDev)

    def reportsThread_start(self):
        self.reportsThread = reportsThread(self.status)
        self.reportsThread.start()

        reports = Reports_class()
        reports.exec_()

    def close_window(self):
        pass

    def open_btn(self):
        pass

    def save_btn(self):
        pass

    def newDev(self):
        #TODO have to fix the device search filter
        QMessageBox.information(self, "New Pump Configuration", "Select the device name")
        
        # Platform specific
        if sys.platform[:3] == 'win':
            dir = '.' # Windows device path?!
        if sys.platform[:3] == 'dar':
            dir = '~/src/python' # Should include this for compatibility issues
        else:
            dir = '.'

        fileObj = QFileDialog.getOpenFileName(self, "New Pump Configuration", dir=dir)
        if fileObj[0]:
            self.ser.port_name = fileObj[0]

    def speed_control(self):
        """function for calling the pump.setPlungerSpeed function"""
        speed = self.speed_spinbox.value()
        pump.setPlungerSpeed(speed)


    def volume_control(self):
        """function for calling the pump.volume_command method."""

        volume = self.volume_prompt.text()
        if self.PushBtn.isChecked():
            direction = "D"
        elif self.PullBtn.isChecked():
            direction = "P"
        else:
            raise Exception("Somethings wrong in the volume_control function")

        (done, answer) = self.pump.volume_command(volume, direction)

        if not done:
            QMessageBox.warning(self, __appname__, answer)
        if done:
            print "plunger own status position" + pump.own_status["plung_pos_mine"]
            print "answer: " + answer

class reportsThread(QThread):

    def __init__(self, status, parent=None):
        super(reportsThread, self).__init__(parent)

        self.status = status

    def run(self):
        #self.reports.Position_Edit.setText(self.status["abs_pos"])
        #self.reports.Top_Velocity_Edit.setText(self.status["top_vel"])
        #self.reports.Cutoff_Velocity_Edit.setText(self.status["cutoff"])
        #self.reports.Actual_Position_Edit.setText(self.status["act_pos"])
        #self.reports.Start_Velocity_Edit.setText(self.status["start"])
        #self.reports.Backlash_Edit.setText(self.status["backlash"])
        #self.reports.Fluid_Sensor_Edit.setText(self.status["fluid"])
        #self.reports.Buffer_Status_Edit.setText(self.status["buffer"])
        #self.reports.Firmware_Edit.setText(self.status["version"])
        #self.reports.Checksm_Edit.setText(self.status["checksum"])
        pass


class Reports_class(QDialog, python_settings.Ui_Dialog):

    def __init__(self, parent=None):
        super(Reports_class, self).__init__(parent)
        self.setupUi(self)

        __appname__ = "Reports Screen"
        self.setWindowTitle(__appname__)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window= MainWindow()
    window.show()
    app.exec_() # Event-loop of the application
