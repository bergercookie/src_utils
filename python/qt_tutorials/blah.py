#!/usr/bin/env python

from PySide.QtGui import *
from PySide.QtCore import *
import sys


class Form(QDialog):

    def __init__(self, parent=None):
        # Automatic thing this is
        super(Form, self).__init__(parent)

        date = self.getdate() #define the getdate method later
        rates = sorted(self.rates.keys())

        dateLabel = QLabel(date)
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates)

        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 100000000.00) # setting the available values of the spinbox
        self.fromSpinBox.setValue(1.00) # Initial value of SpinBox
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates) # adding the fucking items
        self.toLabel = QLabel("1.00")

        # Setting the layout

        grid = QGridLayout()
        grid.addWidget(dateLabel, 0, 0) # 0th row & column
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        self.setLayout(grid)

        my_timer = QTimer(self)
        my_timer.setInterval(5000)
        self.connect(my_timer, SIGNAL("timeout()"), self.kalimera)
        my_timer.start()

    def kalimera(self):
        QMessageBox.warning(self, "Kalimera", "BAAAANNG")


        # setting the behaviour
        """
        I Don't yet know where these specific signals come from SO for
        now I am going to just be using them as-is
        For QComboBox, QSpinBox:
        currentIndexChanged, ValueChanged

        """

        self.connect(self.fromComboBox, SIGNAL("currentIndexChanged(int)"),\
                self.updateUi)
        self.connect(self.toComboBox, SIGNAL("currentIndexChanged(int)"),\
                self.updateUi)
        self.connect(self.fromSpinBox, SIGNAL("ValueChanged(double)"),\
                self.updateUi)
    
    def updateUi(self):
        to = self.toComboBox.currentText()
        from_ = self.fromComboBox.currentText()

        amount = (self.rates[from_] / self.rates[to]) * self.fromSpinBox.value()
        self.toLabel.setText("%0.2f" %amount)

    def getdate(self):
        self.rates = {}

        try:
            date = "Unknown"

            fh = urllib2.urlopen("http://www.bankofcanada.ca/en/markets/csv/exchange_eng.csv")

            for line in fh:
                line = line.rstrip()
                if not line or line.startswith(("#", "Closing")):
                    continue
                
                fields = line.split(",")
                if line.startswith("Date "):
                    date = fields[-1] # see the CSV thing
                else:
                    try:
                        value = float(fields[-1])
                        self.rates[fields[0]] = value
                    except ValueError:
                        pass
            return "Exchange rates date: " + date
        except Exception, e:
            return "Fauluire to download:\n%s" % e

# Well I guess I kind of learn, Aren't I?
# If you don't put it, you don't see anything do you?
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
