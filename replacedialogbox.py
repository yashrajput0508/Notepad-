# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'replacedialogbox.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Find(object):
    def setupUi(self, Find):
        Find.setObjectName("Find")
        Find.resize(445, 187)
        self.label = QtWidgets.QLabel(Find)
        self.label.setGeometry(QtCore.QRect(40, 20, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Find)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Find)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Find)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 60, 201, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Find)
        self.pushButton.setGeometry(QtCore.QRect(340, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Find)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 50, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Find)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 80, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Find)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 110, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Find)
        QtCore.QMetaObject.connectSlotsByName(Find)

    def retranslateUi(self, Find):
        _translate = QtCore.QCoreApplication.translate
        Find.setWindowTitle(_translate("Find", "Dialog"))
        self.label.setText(_translate("Find", "Find what"))
        self.label_2.setText(_translate("Find", "Replace with"))
        self.pushButton.setText(_translate("Find", "Find Next"))
        self.pushButton_2.setText(_translate("Find", "Replace"))
        self.pushButton_3.setText(_translate("Find", "Replace All"))
        self.pushButton_4.setText(_translate("Find", "Cancel"))
