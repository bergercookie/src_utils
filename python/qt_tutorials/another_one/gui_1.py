# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_own.ui'
#
# Created: Thu May  1 13:55:02 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(20, 20, 53, 24))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(5)
        self.spinBox.setObjectName("spinBox")
        self.stackedWidget = QtGui.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(60, 90, 251, 141))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.radioButton = QtGui.QRadioButton(self.page)
        self.radioButton.setGeometry(QtCore.QRect(40, 70, 97, 18))
        self.radioButton.setObjectName("radioButton")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.timeEdit = QtGui.QTimeEdit(self.page_3)
        self.timeEdit.setGeometry(QtCore.QRect(40, 50, 118, 24))
        self.timeEdit.setObjectName("timeEdit")
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.page_3)
        self.dateTimeEdit.setGeometry(QtCore.QRect(30, 90, 194, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalScrollBar = QtGui.QScrollBar(self.page_3)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(40, 10, 160, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.horizontalSlider = QtGui.QSlider(self.page_3)
        self.horizontalSlider.setGeometry(QtCore.QRect(40, 30, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.page_2)
        self.doubleSpinBox.setGeometry(QtCore.QRect(50, 30, 62, 24))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.spinBox_2 = QtGui.QSpinBox(self.page_2)
        self.spinBox_2.setGeometry(QtCore.QRect(150, 30, 53, 24))
        self.spinBox_2.setObjectName("spinBox_2")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox.setToolTip(QtGui.QApplication.translate("Dialog", "Select the tab you want", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("Dialog", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))

