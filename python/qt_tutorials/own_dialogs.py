#!/usr/bin/env python

"""
Dump Dialog Example
See the lines 40, 44  64, 65
This is the "important" shit
"""

# Classic importing shit
import sys
from PySide.QtCore import *
from PySide.QtGui import *


__appname__ = "Dump Dialogs tutorial"

class Program(QDialog):
    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        self.setWindowTitle(__appname__)

        btn = QPushButton("Open Dialog")
        self.label1 = QLabel("Label 1 Result")
        self.label2 = QLabel("Label 1 Result")
        
        # Layout initialization
        layout = QVBoxLayout()
        layout.addWidget(btn)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)

        self.setLayout(layout)

        self.connect(btn, SIGNAL("clicked()"), self.dialog_Open)

    def dialog_Open(self):
        dialog = Dialog()
        #dialog.exec_()
        if dialog.exec_():
            self.label1.setText("Spinbox value is " + str(dialog.spinBox.value())) # the label wants Strings!!
            self.label2.setText("Checkbox is " + str(dialog.checkBox.isChecked()))
        else:
            QMessageBox.warning(self, __appname__, "Dialog Cancelled you Shithead!")



# Defining a new dialog - New Class
class Dialog(QDialog):
     def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog_1")

        # Gonna use them outside the method
        self.checkBox = QCheckBox("Check me Out") # there is a checkBox QWidget as well!
        self.spinBox = QSpinBox()
        buttonOk = QPushButton("OK")
        buttonCancel = QPushButton("Cancel")

        layout = QGridLayout() # Multiple rows, cols
        layout.addWidget(self.spinBox, 0, 0)
        layout.addWidget(self.checkBox, 0, 1)
        layout.addWidget(buttonCancel) # let it decide where to put it
        layout.addWidget(buttonOk)
        self.setLayout(layout)
       
        # see line 35!
        self.connect(buttonOk, SIGNAL("clicked()"), SLOT("accept()")) # OK is pressed, 0 returned!
        self.connect(buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()")) # nothing happens !


app = QApplication(sys.argv)
form = Program()
form.show()
sys.exit(app.exec_())
