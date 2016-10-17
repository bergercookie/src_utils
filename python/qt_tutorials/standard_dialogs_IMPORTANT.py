#!/usr/bin/env python

"""
*** Comments ***
Dump dialogs do not know anything about their surroundings

Standard Dialogs:
    Use a dictionary to pass the values to the Dialog Box from the mainProgram window
    The gaol is to pass data between the different dialog windows!
"""

# Classic importing shit
import sys
from PySide.QtCore import *
from PySide.QtGui import *


__appname__ = "Standard Dialogs tutorial"

class Program(QDialog):
    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        self.setWindowTitle(__appname__)

        btn = QPushButton("Open Dialog")
        self.mainSpinBox = QSpinBox()
        self.mainCheckBox = QCheckBox("Main Checkbox Value")
        
        # Layout initialization
        layout = QVBoxLayout()
        layout.addWidget(btn)
        layout.addWidget(self.mainSpinBox)
        layout.addWidget(self.mainCheckBox)

        self.setLayout(layout)

        self.connect(btn, SIGNAL("clicked()"), self.dialog_Open)

    def dialog_Open(self):
        initValues = {"mainSpinBox" : self.mainSpinBox.value(), "mainCheckBox": self.mainCheckBox.isChecked()}
        dialog = Dialog(initValues) # pass a dictionary as a parameter
        #dialog.exec_()
        if dialog.exec_():
            self.mainSpinBox.setValue(dialog.spinBox.value())
            self.mainCheckBox.setChecked(dialog.checkBox.isChecked())


# Defining a new dialog - New Class
class Dialog(QDialog):
    def __init__(self, initValues, parent=None):
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

        self.spinBox.setValue(initValues["mainSpinBox"])
        self.checkBox.setChecked(initValues["mainCheckBox"])
       
        # see line 35!
        self.connect(buttonOk, SIGNAL("clicked()"), SLOT("accept()")) # OK is pressed, 0 returned!
        self.connect(buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()")) # nothing happens !
    # Overwrite the Accept builting method

    def accept(self):
        class GreaterThanFive(Exception): pass
        class IsZero(Exception): pass

        try:
            if self.spinBox.value() > 5:
                raise GreaterThanFive, ("The SpinBox valuecannot be greater than 5")
            elif self.spinBox.value() == 0:
                raise IsZero, ("The SpinBox value cannot be equal to 0")
            else:
                QDialog.accept(self) # same signal as in L73
        
        except GreaterThanFive, e:
            QMessageBox.warning(self, __appname__, str(e))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return False
        except IsZero, e:
            QMessageBox.warning(self, __appname__, str(e))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return False





app = QApplication(sys.argv)
form = Program()
form.show()
sys.exit(app.exec_())
