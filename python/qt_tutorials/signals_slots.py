#!/usr/bin/env python

# Same old imports first
import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # dial widget
        dial = QDial() # Something like an analog dialing phone
        dial.setNotchesVisible(True) # let the notches be visible
        
        # spinbox widget
        spinbox = QSpinBox()

        # label widget
        label = QLabel("kalimera lae mou") # added a label just for the fun of things

        # Creating the layout
        layout = QHBoxLayout()
        layout.addWidget(spinbox)
        layout.addWidget(dial)
        layout.addWidget(label)
        self.setLayout(layout)
        self.connect(dial, SIGNAL("valueChanged(int)"), spinbox.setValue) # the dial when changed emits the value changed signal to the spinbox by calling the setValue function with the int as a parameter!!!
        self.connect(spinbox, SIGNAL("valueChanged(int)"), dial.setValue)

        self.setWindowTitle("Signals and Slots")

# Same old shit last
app = QApplication(sys.argv)
form = Form()
form.show()
sys.exit(app.exec_())

