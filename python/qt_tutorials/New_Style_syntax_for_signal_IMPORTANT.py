#!/usr/bin/env python

import sys
from PySide.QtGui import *
from PySide.QtCore import *

class MainDialog(QDialog):
    
    # Builtin Signal Class?!
    # WATCH tutorial 16 for even more!! USEFUL STUFF!
    # IMPORTANT! I can pass strings, ints, floats, WHATEVER! but I have to state it inside the parentheses
    myOwnSignal = Signal(str)

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)

        layout = QVBoxLayout()
        self.btn1 = QPushButton("Button!")

        layout.addWidget(self.btn1)
        self.setLayout(layout)

        # the old style Signal mechanism
        # NO error notification, Not Pythonic at all
        #self.connect(self.btn1, SIGNAL("clicked()"), self.btn1clicked)
        #self.connect(self, SIGNAL("myOwnSignal()"), self.myOwnSignalEmmitted)
        self.myOwnSignal.connect(self.myOwnSignalEmmitted)

        # New Style signal mechanism, MUCH BETTER
        # BUTTON.SIGNAL.CONNECTED_TO(FUNCION)
        self.btn1.clicked.connect(self.btn1clicked)

    def btn1clicked(self):
        #QMessageBox.information(self, "Hello", "Button 1 clicked")
        # Old style
        #self.emit(SIGNAL("myOwnSignal(QString)", "Whatever." )

        self.myOwnSignal.emit("Whatever") # New style shit!! 
    
    def myOwnSignalEmmitted(self, text_emitted):
        print "kalimera"
        QMessageBox.information(self, "kalimera Window", text_emitted)

app = QApplication(sys.argv)
form = MainDialog()
form.show()
sys.exit(app.exec_())
