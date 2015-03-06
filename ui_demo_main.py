# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_main.ui'
#
# Created: Mon Mar 02 16:27:28 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(809, 638)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 761, 581))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 2)
        self.epushButton = QtGui.QPushButton(self.widget)
        self.epushButton.setObjectName(_fromUtf8("epushButton"))
        self.gridLayout.addWidget(self.epushButton, 0, 2, 1, 1)
        self.elineEdit = QtGui.QLineEdit(self.widget)
        self.elineEdit.setText(_fromUtf8(""))
        self.elineEdit.setObjectName(_fromUtf8("elineEdit"))
        self.gridLayout.addWidget(self.elineEdit, 1, 0, 1, 1)
        self.echeckBox_2 = QtGui.QCheckBox(self.widget)
        self.echeckBox_2.setObjectName(_fromUtf8("echeckBox_2"))
        self.gridLayout.addWidget(self.echeckBox_2, 1, 1, 1, 1)
        self.dpushButton = QtGui.QPushButton(self.widget)
        self.dpushButton.setObjectName(_fromUtf8("dpushButton"))
        self.gridLayout.addWidget(self.dpushButton, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textEdit = QtGui.QTextEdit(self.widget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        self.textEdit_2 = QtGui.QTextEdit(self.widget)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.horizontalLayout.addWidget(self.textEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "登录报文", None))
        self.epushButton.setText(_translate("MainWindow", "编码", None))
        self.echeckBox_2.setText(_translate("MainWindow", "加解密", None))
        self.dpushButton.setText(_translate("MainWindow", "解码", None))

