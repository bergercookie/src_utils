#!/usr/bin/env python

import sys
from PySide.QtGui import *
from PySide.QtCore import *

import something_gui_python as sm
import random
from time import sleep

__appname__ = "something_own"

class MyDialog(QDialog, sm.Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent=None)
        self.setupUi(self)

        self.buttonBox.rejected.connect(self.reject_function)
        self.buttonBox.accepted.connect(self.accept_function)
        self.Tab1_Push_Button.clicked.connect(self.tabswitch)
        print self.stackedWidget.currentIndex()

    def reject_function(self):
        sys.exit()

    def accept_function(self):
        QMessageBox.information(self, __appname__, "You pressed the ok")

    def tabswitch(self):
        QMessageBox.warning(self, __appname__, "kalimera")
        #i = random.randrange(1, 3)
        #print i
        for i in range(3, -1, -1):
            sleep(1)
            self.stackedWidget.setCurrentIndex(i)
            print "kalimera"


app = QApplication(sys.argv)
form = MyDialog()
form.show()
sys.exit(app.exec_())
