#!/usr/bin/env python

"""
*** ADDITIONAL COMMENTS ***

"""

import sys
from PySide.QtCore import *
from PySide.QtGui import * # this is the one you most times need

__appname__ = "Eight Video"

class Program(QDialog):

    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        # four buttons 
        openButton = QPushButton("Open")
        saveButton = QPushButton("Save")
        dirButton = QPushButton("Other")
        closeButton = QPushButton("Close...")

        self.connect(openButton, SIGNAL("clicked()"), self.open)
        self.connect(saveButton, SIGNAL("clicked()"), self.save)
        
        # layout initialization
        layout = QVBoxLayout()
        layout.addWidget(openButton)
        layout.addWidget(closeButton)
        layout.addWidget(saveButton)
        layout.addWidget(dirButton)

        self.setLayout(layout)

    # Define the behaviors
    def open(self):
        dir = "." # Should include this for compatibility issues

        fileObj = QFileDialog.getOpenFileName(self, __appname__ + \
                " Open File Dialog", dir=dir, filter="Text files (*.txt)") # see the available options in the documentation
        print fileObj
        print type(fileObj)
        
        file1 = open(fileObj[0], mode='r')
        read = file1.readlines()
        print read
        file1.close()

    def save(self):
        dir = "."

        fileObj = QFileDialog.getSaveFileName(self, __appname__, \
                dir=dir, filter="Text Files (*.txt)")

        contents = "Hello from  nikos' Era!!"
        fileName = fileObj[0]
        file1 = open(fileName, mode="w")
        file1.write(contents)
        file1.close()




app = QApplication(sys.argv)
form = Program()
form.show()
app.exec_()


