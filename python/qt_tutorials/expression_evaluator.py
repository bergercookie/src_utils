#!/usr/bin/env python

import sys
from PySide.QtCore import *
from PySide.QtGui import *

from math import *

class Form(QDialog):
    # Pretty straightforward
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll() # ble grammi gia ameso svisimo

        layout = QVBoxLayout()
        # Adding the above features
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)

        self.lineedit.setFocus() # directly type in the textbox without having to press it 

        self.connect(self.lineedit, SIGNAL("returnPressed()"), self.updateUi)
        # the Ui method isn't implemented yet

        self.setWindowTitle("Calculate")
    
    def updateUi(self):
        try:
            text = self.lineedit.text()
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
            
        except:
            self.browser.append("<font color=red>%s is invalid</font>" % text)

# Usual stuff
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
        
