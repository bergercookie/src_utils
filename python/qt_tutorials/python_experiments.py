#!/usr/bin/env python

import serial
import sys
from PySide.QtGui import *
from PySide.QtCore import *

class Program(QDialog):

    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        # four buttons 
        self.layout = QVBoxLayout()
        openButton = QPushButton("Open")
        saveButton = QPushButton("Save")
        dirButton = QPushButton("Other")
        closeButton = QPushButton("Close...")

        self.layout.addWidget(openButton)
        self.layout.addWidget(saveButton)
        self.layout.addWidget(closeButton)
        self.layout.addWidget(dirButton)

        self.setLayout(self.layout)

       
        openButton.setCheckable(True)
        print openButton.isFlat()
        self.connect(openButton, SIGNAL("clicked()"), self.open_fun)

    def open_fun(self):
        print "Im In" + str(openButton.isFlat())

app = QApplication(sys.argv)
form = Program()
form.show()
app.exec_()
