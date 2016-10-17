# Thu May 29 02:59:41 EEST 2014, nickkouk

# proper division for python 2.7
from __future__ import division

# Usual importing stuff for PySide
from PySide.QtGui import *
from PySide.QtCore import *

# Module imports
import sys
import os
from serial.tools.list_ports import comports

# Qt-Designer compiled python code
import python_gui
import python_settings
import history_settings
import device_configuration

class HistoryDialog(QDialog, history_settings.Ui_Dialog):
    def __init__(self, pump, parent = None):
        super(HistoryDialog, self).__init__(parent)
        self.setupUi(self) 

        self.pump = pump
        self.__appname__ = "Commands History"
        self.setWindowTitle(self.__appname__)

        self.connect(self.refresh_Btn, SIGNAL("clicked()"), self.refresh)
        self.connect(self.commands_only, SIGNAL("clicked()"), \
                self.refresh)



    def refresh(self):
        wanted = self.pump.history
        wanted_string = ''
        if self.commands_only.isChecked():
            for i in wanted:
                wanted_string += "{}\\r\n".format(i[:-1])
        else:
            for i in range(len(wanted)):
                wanted_string += "{0}:\t {1}\\r\n".format(i+1, wanted[i][:-1])

        self.history_edit.setPlainText(wanted_string)

class ReportsDialog(QDialog, python_settings.Ui_Dialog):

    def __init__(self, pump, parent=None):
        super(ReportsDialog,  self).__init__(parent)
        self.setupUi(self)

        self.__appname__ = "Reports Screen"
        self.setWindowTitle(self.__appname__)
        self.pump = pump
        self.pump.refresh = True

         # Set up a timer for periodical refresh of the pump settings report
        self.refreshQtimer = QTimer(self)
        self.refreshQtimer.setInterval(2000)
        self.connect(self.refreshQtimer, SIGNAL("timeout()"), self.refresh)
        self.refreshQtimer.start()
        # Need to stop the timer when the window closes
        self.connect(self, SIGNAL("rejected()"), self.refreshQtimer.stop)

        self.refresh_interval_edit.setText("%s"\
                % int((self.refreshQtimer.interval() / 1000)))

        # Setting the refresh interval manually
        self.connect(self.refresh_interval_edit,\
                SIGNAL("returnPressed()"),\
                self.setRefreshTime)

    def refresh(self):
        """ The refresh function shows the pump major statistics.

        The refresh function is periodically run using the QTimer refreshQtimer
        When the timer timeouts the stats are fetched from the pump
        """
        stats = self.pump.status

        self.Actual_Position_Edit.setText(stats["actual_pos"])
        self.Backlash_Steps_Edit.setText(stats["backlash_steps"])
        self.Cutoff_Velocity_Edit.setText(stats["cutoff_vel"])
        self.Position_Edit.setText(stats["absolute_pos"])
        self.Start_Velocity_Edit.setText(stats["starting_vel"])
        self.Top_Velocity_Edit.setText(stats["top_vel"])
        self.Checksum_Edit.setText(stats["checksum"])
        self.Fluid_Sensor_Edit.setText(stats["fluid_sensor"])
        self.Buffer_Status_Edit.setText(stats["buffer_status"])
        self.Version_Edit.setText(stats["version"])

    def setRefreshTime(self):
        text = self.refresh_interval_edit.text()
        if text.isdigit():
            self.pump.interval = int(text)
            self.pump.setTimer_interval()
            self.refreshQtimer.setInterval(\
                    eval(text) * 1000)

            self.refresh_interval_edit.setText("%s"\
                    % int((self.refreshQtimer.interval() / 1000)))
        else: 
            QMessageBox.warning(self, self.__appname__, "Not a valid input")

        self.refresh_interval_edit.selectAll()

    def tick_refresh(self):
        if self.noRefresh.isChecked():
            self.pump.cancel_timer()
        else:
            self.pump.refresh = True
            self.pump.update_values()
    
class NewDevDialog(QDialog, device_configuration.Ui_Dialog):

    def __init__(self, pump, parent=None):
        super(NewDevDialog,  self).__init__(parent)
        self.setupUi(self)

        self.__appname__ = "Device Configuration"
        self.comports = comports
        self.pump = pump

        ports_available = list(self.comports())
        for i in range(len(ports_available)):
            self.listWidget.addItem(ports_available[i][0])

    def connect_with_port(self):
        """Passes the selected item into the accept_new method of the pump."""
        port = self.listWidget.currentItem().text()
        self.pump.accept_new(port)
