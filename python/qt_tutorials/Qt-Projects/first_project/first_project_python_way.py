#!/usr/bin/env python

"""
This shit is a real revolution!
remember how to syntax the whole thing
Congratulations
"""
import sys
from PySide.QtGui import *
from PySide.QtCore import *

import first_project

class MainDialog(QDialog, first_project.Ui_MainDialog):
    def __init__(self, parent = None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        # this is the update with regards to the Designer project
        self.connect(self.ShowButton, SIGNAL("clicked()"), self.processdata)

    def processdata(self):
        QMessageBox.information(self, "Hello World", "Hello there honey"\
                + self.nameEdit.text())




app = QApplication(sys.argv)
form = MainDialog()
form.show()
sys.exit(app.exec_())
