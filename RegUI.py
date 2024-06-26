# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_reg.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_regedit(object):
    def setupUi(self, regedit):
        regedit.setObjectName("regedit")
        regedit.resize(522, 271)
        regedit.setStyleSheet("background-color: rgb(78, 85, 92);")
        self.user_lineEdit = QtWidgets.QLineEdit(regedit)
        self.user_lineEdit.setGeometry(QtCore.QRect(270, 50, 221, 35))
        self.user_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.pwd_lineEdit = QtWidgets.QLineEdit(regedit)
        self.pwd_lineEdit.setGeometry(QtCore.QRect(270, 130, 221, 35))
        self.pwd_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pwd_lineEdit.setObjectName("pwd_lineEdit")
        self.reg_pushButton = QtWidgets.QPushButton(regedit)
        self.reg_pushButton.setGeometry(QtCore.QRect(270, 210, 221, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.reg_pushButton.setFont(font)
        self.reg_pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 227, 255, 255), stop:1 rgba(137, 59, 245, 255));\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"微软雅黑\";")
        self.reg_pushButton.setObjectName("reg_pushButton")
        self.label = QtWidgets.QLabel(regedit)
        self.label.setGeometry(QtCore.QRect(0, 0, 231, 271))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(regedit)
        self.label_2.setGeometry(QtCore.QRect(270, 20, 71, 31))
        self.label_2.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(regedit)
        self.label_3.setGeometry(QtCore.QRect(270, 100, 71, 21))
        self.label_3.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(regedit)
        self.reg_pushButton.clicked.connect(regedit.slot_ok) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(regedit)

    def retranslateUi(self, regedit):
        _translate = QtCore.QCoreApplication.translate
        regedit.setWindowTitle(_translate("regedit", "新用户注册"))
        self.user_lineEdit.setText(_translate("regedit", "admin"))
        self.pwd_lineEdit.setText(_translate("regedit", "123456"))
        self.reg_pushButton.setText(_translate("regedit", "注册"))
        self.label_2.setText(_translate("regedit", "用户名："))
        self.label_3.setText(_translate("regedit", "密   码："))
