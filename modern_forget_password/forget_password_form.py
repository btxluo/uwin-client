# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pyProj\new-uwin\modern_forget_password\forget_password_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from modern_gui.qt_core import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(421, 391)
        Form.setStyleSheet("QWidget{background-color: rgb(44,49,60);\n"
"border-radius: 8px;\n"
"border: 2px solid #343b48;}")
        self.lineEditAccount = QLineEdit(Form)
        self.lineEditAccount.setGeometry(QRect(150, 80, 226, 40))
        self.lineEditAccount.setMinimumSize(QSize(0, 40))
        self.lineEditAccount.setStyleSheet("QLineEdit {\n"
"      color: rgb(220,225,236);\n"
"      font: 15pt \"Verdana\";\n"
"      border: None;\n"
"      border-bottom-color: white;\n"
"      border-radius: 8px;\n"
"      padding: 0 8px;\n"
"      background: rgb(52,59,72);\n"
"      selection-background-color: darkgray;\n"
"}")
        self.lineEditAccount.setObjectName("lineEditAccount")
        self.lineEditPasswd = QLineEdit(Form)
        self.lineEditPasswd.setGeometry(QRect(150, 140, 226, 40))
        self.lineEditPasswd.setMinimumSize(QSize(0, 40))
        self.lineEditPasswd.setStyleSheet("QLineEdit {\n"
"      color: rgb(220,225,236);\n"
"      font: 15pt \"Verdana\";\n"
"      border: None;\n"
"      border-bottom-color: white;\n"
"      border-radius: 8px;\n"
"      padding: 0 8px;\n"
"      background: rgb(52,59,72);\n"
"      selection-background-color: darkgray;\n"
"}")
        self.lineEditPasswd.setObjectName("lineEditPasswd")
        self.lineEditPasswd_2 = QLineEdit(Form)
        self.lineEditPasswd_2.setGeometry(QRect(150, 220, 226, 40))
        self.lineEditPasswd_2.setMinimumSize(QSize(0, 40))
        self.lineEditPasswd_2.setStyleSheet("QLineEdit {\n"
"      color: rgb(220,225,236);\n"
"      font: 15pt \"Verdana\";\n"
"      border: None;\n"
"      border-bottom-color: white;\n"
"      border-radius: 8px;\n"
"      padding: 0 8px;\n"
"      background: rgb(52,59,72);\n"
"      selection-background-color: darkgray;\n"
"}")
        self.lineEditPasswd_2.setObjectName("lineEditPasswd_2")
        self.pushButtonRegister = QPushButton(Form)
        self.pushButtonRegister.setGeometry(QRect(50, 220, 83, 45))
        self.pushButtonRegister.setMinimumSize(QSize(0, 45))
        font = QFont()
        font.setFamily("yahei")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QFont.Weight(50))
        self.pushButtonRegister.setFont(font)
        self.pushButtonRegister.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 17pt \"yahei\";\n"
"border: 2px solid rgb(79,159,238);\n"
"padding: 5px;\n"
"border-radius: 8px;\n"
"opacity: 200;\n"
"")
        self.pushButtonRegister.setDefault(False)
        self.pushButtonRegister.setFlat(False)
        self.pushButtonRegister.setObjectName("pushButtonRegister")
        self.pushButtonLogin = QPushButton(Form)
        self.pushButtonLogin.setGeometry(QRect(60, 290, 315, 45))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonLogin.sizePolicy().hasHeightForWidth())
        self.pushButtonLogin.setSizePolicy(sizePolicy)
        self.pushButtonLogin.setMinimumSize(QSize(0, 45))
        font = QFont()
        font.setFamily("yahei")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QFont.Weight(50))
        font.setKerning(True)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setAutoFillBackground(False)
        self.pushButtonLogin.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 17pt \"yahei\";\n"
"border: 2px solid rgb(79,159,238);\n"
"padding: 5px;\n"
"border-radius: 8px;\n"
"opacity: 200;\n"
"")
        self.pushButtonLogin.setAutoDefault(False)
        self.pushButtonLogin.setDefault(False)
        self.pushButtonLogin.setFlat(False)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.label = QLabel(Form)
        self.label.setGeometry(QRect(50, 80, 91, 41))
        self.label.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 17pt \"yahei\";\n"
"padding: 5px;\n"
"border-radius: 8px;\n"
"opacity: 200;")
        self.label.setObjectName("label")
        self.label_2 = QLabel(Form)
        self.label_2.setGeometry(QRect(30, 140, 111, 41))
        self.label_2.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 17pt \"yahei\";\n"
"padding: 5px;\n"
"border-radius: 8px;\n"
"opacity: 200;")
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setGeometry(QRect(380, 10, 35, 25))
        self.pushButton_3.setMinimumSize(QSize(35, 25))
        self.pushButton_3.setMaximumSize(QSize(35, 25))
        self.pushButton_3.setStyleSheet("color: white;\n"
"font: 12pt \"Arial\";\n"
"")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "??????"))
        self.pushButtonRegister.setText(_translate("Form", "?????????"))
        self.pushButtonLogin.setText(_translate("Form", "????????????"))
        self.label.setText(_translate("Form", "?????????"))
        self.label_2.setText(_translate("Form", "????????????"))
        self.pushButton_3.setText(_translate("Form", "X"))
