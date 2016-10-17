#!/usr/bin/env python

import sys
from PySide.QtGui import *
from PySide.QtCore import *

import gui_1

class first_dialog(QDialog, gui_1.Ui_Dialog):
    def __init__(self, parent=None):
        super(first_dialog, self).__init__(parent)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.spinBox.valueChanged.connect(self.change_widget)

    def change_widget(self, value_int):
        self.stackedWidget.setCurrentIndex(value_int-1)


app = QApplication(sys.argv)
form = first_dialog()
form.show()
app.exec_()
