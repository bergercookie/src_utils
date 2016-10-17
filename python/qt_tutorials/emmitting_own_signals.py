#!/usr/bin/env python

import sys
from PySide.QtGui import *
from PySide.QtCore import *

"""
the goal of this tutorial is to learn how to emit your own signals
use the self.emit(SIGNAL(signal), slot) mechanism
"""

class ZeroSpinBox(QSpinBox):

    zeros = 0

    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)

        self.connect(self, SIGNAL("valueChanged(int)"), self.checkzero) # the self is the ZeroSpinbox

    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.emit(SIGNAL("atzero(int)"), self.zeros)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # dial widget
        dial = QDial() # Something like an analog dialing phone
        dial.setNotchesVisible(True) # let the notches be visible
        
        # spinbox widget
        zerospinbox =ZeroSpinBox()

        # label widget
        label = QLabel("kalimera lae mou") # added a label just for the fun of things

        # Creating the layout
        layout = QHBoxLayout()
        layout.addWidget(zerospinbox)
        layout.addWidget(dial)
        layout.addWidget(label)
        self.setLayout(layout)
        self.connect(dial, SIGNAL("valueChanged(int)"), zerospinbox.setValue) # the dial when changed emits the value changed signal to the spinbox by calling the setValue function with the int as a parameter!!!
        self.connect(zerospinbox, SIGNAL("valueChanged(int)"), dial.setValue)

        self.connect(zerospinbox, SIGNAL("atzero(int)"), self.announce)
        self.setWindowTitle("Signals and Slots")

    def announce(self, zeros):
        print "%s times it has been at zero" % zeros

# Same old shit last
app = QApplication(sys.argv)
form = Form()
form.show()
sys.exit(app.exec_())

