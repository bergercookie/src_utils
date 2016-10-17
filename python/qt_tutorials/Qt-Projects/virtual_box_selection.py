# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VirtualBox OS Selection.ui'
#
# Created: Sun Apr 27 13:33:36 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(500, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/build-your-own-linux-distribution.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainDialog.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(MainDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ArchButton = QtGui.QPushButton(MainDialog)
        font = QtGui.QFont()
        font.setFamily("Baghdad")
        font.setPointSize(15)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.ArchButton.setFont(font)
        self.ArchButton.setCursor(QtCore.Qt.CrossCursor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icn.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ArchButton.setIcon(icon1)
        self.ArchButton.setObjectName("ArchButton")
        self.horizontalLayout.addWidget(self.ArchButton)
        self.FedoraButton = QtGui.QPushButton(MainDialog)
        font = QtGui.QFont()
        font.setFamily("Baghdad")
        font.setPointSize(15)
        self.FedoraButton.setFont(font)
        self.FedoraButton.setCursor(QtCore.Qt.CrossCursor)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icon1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FedoraButton.setIcon(icon2)
        self.FedoraButton.setObjectName("FedoraButton")
        self.horizontalLayout.addWidget(self.FedoraButton)
        self.WindowsButton = QtGui.QPushButton(MainDialog)
        font = QtGui.QFont()
        font.setFamily("Baghdad")
        font.setPointSize(15)
        self.WindowsButton.setFont(font)
        self.WindowsButton.setCursor(QtCore.Qt.CrossCursor)
        self.WindowsButton.setIcon(icon)
        self.WindowsButton.setObjectName("WindowsButton")
        self.horizontalLayout.addWidget(self.WindowsButton)

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(QtGui.QApplication.translate("MainDialog", "Pick an OS", None, QtGui.QApplication.UnicodeUTF8))
        self.ArchButton.setText(QtGui.QApplication.translate("MainDialog", "Load Arch", None, QtGui.QApplication.UnicodeUTF8))
        self.FedoraButton.setText(QtGui.QApplication.translate("MainDialog", "Load Fedora", None, QtGui.QApplication.UnicodeUTF8))
        self.WindowsButton.setText(QtGui.QApplication.translate("MainDialog", "Load Windows", None, QtGui.QApplication.UnicodeUTF8))

import resource_file_rc
