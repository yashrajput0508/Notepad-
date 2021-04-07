# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'go.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Go(object):
    def setupUi(self, Go):
        Go.setObjectName("Go")
        Go.resize(306, 125)
        self.label = QtWidgets.QLabel(Go)
        self.label.setGeometry(QtCore.QRect(50, 20, 61, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Go)
        self.lineEdit.setGeometry(QtCore.QRect(50, 50, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Go)
        self.pushButton.setGeometry(QtCore.QRect(50, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Go)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Go)
        QtCore.QMetaObject.connectSlotsByName(Go)

    def retranslateUi(self, Go):
        _translate = QtCore.QCoreApplication.translate
        Go.setWindowTitle(_translate("Go", "Dialog"))
        self.label.setText(_translate("Go", "Line Number"))
        self.pushButton.setText(_translate("Go", "Go"))
        self.pushButton_2.setText(_translate("Go", "Cancel"))
