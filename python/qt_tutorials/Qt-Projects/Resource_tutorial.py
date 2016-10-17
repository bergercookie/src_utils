#!/usr/bin/env python

import sys
from PySide.QtCore import *
from PySide.QtGui import *

import virtual_box_selection

class MainDialog(QDialog, virtual_box_selection.Ui_MainDialog):
    
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
form = MainDialog()
form.show()
sys.exit(app.exec_())
