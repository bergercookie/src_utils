# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firts_project.ui'
#
# Created: Sat Apr 26 14:05:04 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(400, 300)
        self.nameEdit = QtGui.QLineEdit(MainDialog)
        self.nameEdit.setGeometry(QtCore.QRect(20, 20, 171, 16))
        self.nameEdit.setInputMask("")
        self.nameEdit.setText("")
        self.nameEdit.setCursorPosition(0)
        self.nameEdit.setObjectName("nameEdit")
        self.ShowButton = QtGui.QPushButton(MainDialog)
        self.ShowButton.setGeometry(QtCore.QRect(200, 10, 110, 32))
        self.ShowButton.setObjectName("ShowButton")

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)
        MainDialog.setTabOrder(self.ShowButton, self.nameEdit)

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(QtGui.QApplication.translate("MainDialog", "Main Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.nameEdit.setPlaceholderText(QtGui.QApplication.translate("MainDialog", "What is your fav Color?", None, QtGui.QApplication.UnicodeUTF8))
        self.ShowButton.setText(QtGui.QApplication.translate("MainDialog", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

