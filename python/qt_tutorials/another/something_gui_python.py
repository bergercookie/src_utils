# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'something_like_it.ui'
#
# Created: Thu May  1 11:48:45 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 334)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(270, 300, 164, 32))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 20, 401, 80))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
"QToolButton {\n"
"background-color : transparent;\n"
"border : none;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButtonpressed {\n"
"background-color:rgb[193, 210, 238];\n"
"}\n"
"")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Tab1_Push_Button = QtGui.QPushButton(self.frame)
        self.Tab1_Push_Button.setGeometry(QtCore.QRect(9, 30, 91, 32))
        self.Tab1_Push_Button.setCursor(QtCore.Qt.CrossCursor)
        self.Tab1_Push_Button.setStatusTip("")
        self.Tab1_Push_Button.setCheckable(True)
        self.Tab1_Push_Button.setAutoExclusive(True)
        self.Tab1_Push_Button.setDefault(False)
        self.Tab1_Push_Button.setObjectName("Tab1_Push_Button")
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 30, 91, 32))
        self.pushButton_3.setCursor(QtCore.Qt.CrossCursor)
        self.pushButton_3.setStatusTip("")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtGui.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 30, 91, 32))
        self.pushButton_4.setCursor(QtCore.Qt.CrossCursor)
        self.pushButton_4.setStatusTip("")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoExclusive(True)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 30, 110, 32))
        self.pushButton_2.setCursor(QtCore.Qt.CrossCursor)
        self.pushButton_2.setStatusTip("")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget = QtGui.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 110, 411, 161))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.tabWidget = QtGui.QTabWidget(self.page)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 401, 141))
        self.tabWidget.setStyleSheet("QCheckBox{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.checkBox_3 = QtGui.QCheckBox(self.tab_5)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 70, 85, 18))
        self.checkBox_3.setObjectName("checkBox_3")
        self.comboBox_2 = QtGui.QComboBox(self.tab_5)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 10, 221, 26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.checkBox_4 = QtGui.QCheckBox(self.tab_5)
        self.checkBox_4.setGeometry(QtCore.QRect(150, 70, 85, 18))
        self.checkBox_4.setObjectName("checkBox_4")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.tab_6)
        self.dateTimeEdit.setGeometry(QtCore.QRect(110, 40, 194, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.dockWidget = QtGui.QDockWidget(self.tab_7)
        self.dockWidget.setGeometry(QtCore.QRect(10, -20, 120, 80))
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.spinBox = QtGui.QSpinBox(self.tab_7)
        self.spinBox.setGeometry(QtCore.QRect(230, 40, 53, 24))
        self.spinBox.setObjectName("spinBox")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab_8)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 20, 104, 78))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.comboBox_3 = QtGui.QComboBox(self.tab_8)
        self.comboBox_3.setGeometry(QtCore.QRect(220, 50, 104, 26))
        self.comboBox_3.setObjectName("comboBox_3")
        self.tabWidget.addTab(self.tab_8, "")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.Tab1_Push_Button, QtCore.SIGNAL("pressed()"), self.tabWidget.update)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab1_Push_Button.setToolTip(QtGui.QApplication.translate("Dialog", "This is a tab option", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab1_Push_Button.setWhatsThis(QtGui.QApplication.translate("Dialog", "Press to select this tab\\", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab1_Push_Button.setText(QtGui.QApplication.translate("Dialog", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setToolTip(QtGui.QApplication.translate("Dialog", "This is a tab option", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setWhatsThis(QtGui.QApplication.translate("Dialog", "Press to select this tab\\", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Dialog", "Tab 3", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setToolTip(QtGui.QApplication.translate("Dialog", "This is a tab option", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setWhatsThis(QtGui.QApplication.translate("Dialog", "Press to select this tab\\", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Dialog", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setToolTip(QtGui.QApplication.translate("Dialog", "This is a tab option", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setWhatsThis(QtGui.QApplication.translate("Dialog", "Press to select this tab\\", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "Tab 4", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("Dialog", "Setting 1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("Dialog", "Setting 1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(1, QtGui.QApplication.translate("Dialog", "Setting 2", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("Dialog", "Setting 2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("Dialog", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtGui.QApplication.translate("Dialog", "Robot", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QtGui.QApplication.translate("Dialog", "Tracking", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QtGui.QApplication.translate("Dialog", "Social", None, QtGui.QApplication.UnicodeUTF8))

