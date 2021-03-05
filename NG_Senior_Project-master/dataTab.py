# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataTab.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataWindow(object):
    def setupUi(self, DataWindow):
        DataWindow.setObjectName("DataWindow")
        DataWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(DataWindow)
        self.centralwidget.setObjectName("centralwidget")
        DataWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        DataWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataWindow)
        self.statusbar.setObjectName("statusbar")
        DataWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DataWindow)
        QtCore.QMetaObject.connectSlotsByName(DataWindow)

    def retranslateUi(self, DataWindow):
        _translate = QtCore.QCoreApplication.translate
        DataWindow.setWindowTitle(_translate("DataWindow", "MainWindow"))

