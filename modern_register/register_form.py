# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Uproject\new-uwin\modern_register\register_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from modern_gui.qt_core import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(619, 496)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("QWidget {background-color: rgb(44,49,60);\n"
"border-radius: 8px;\n"
"border: 2px solid #343b48;}")
        self.label_3 = QLabel(Form)
        self.label_3.setGeometry(QRect(115, 102, 83, 44))
        self.label_3.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 17pt \"Verdana\";\n"
"padding: 5px;\n"
"border-radius: 8px;\n"
"opacity: 200;")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEditPasswd_2 = QLineEdit(Form)
        self.lineEditPasswd_2.setGeometry(QRect(204, 161, 355, 40))
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
        self.lineEditPasswd_2.setInputMethodHints(Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.lineEditPasswd_2.setEchoMode(QLineEdit.Password)
        self.lineEditPasswd_2.setObjectName("lineEditPasswd_2")
        self.label_4 = QLabel(Form)
        self.label_4.setGeometry(QRect(59, 161, 139, 44))
        self.label_4.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 17pt \"Verdana\";\n"
"padding: 5px;\n"
"border-radius: 8px;\n"
"opacity: 200;")
        self.label_4.setObjectName("label_4")
        self.lineEditVerify = QLineEdit(Form)
        self.lineEditVerify.setGeometry(QRect(200, 280, 355, 40))
        self.lineEditVerify.setMinimumSize(QSize(0, 40))
        self.lineEditVerify.setStyleSheet("QLineEdit {\n"
"      color: rgb(220,225,236);\n"
"      font: 15pt \"Verdana\";\n"
"      border: None;\n"
"      border-bottom-color: white;\n"
"      border-radius: 8px;\n"
"      padding: 0 8px;\n"
"      background: rgb(52,59,72);\n"
"      selection-background-color: darkgray;\n"
"}")
        self.lineEditVerify.setObjectName("lineEditVerify")
        self.pushButtonRegister = QPushButton(Form)
        self.pushButtonRegister.setGeometry(QRect(59, 369, 500, 48))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRegister.sizePolicy().hasHeightForWidth())
        self.pushButtonRegister.setSizePolicy(sizePolicy)
        self.pushButtonRegister.setMinimumSize(QSize(0, 45))
        font = QFont()
        font.setFamily("Verdana")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QFont.Weight(50))
        font.setKerning(True)
        self.pushButtonRegister.setFont(font)
        self.pushButtonRegister.setAutoFillBackground(False)
        self.pushButtonRegister.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 17pt \"Verdana\";\n"
"border: 2px solid rgb(79,159,238);\n"
"padding: 5px;\n"
"border-radius: 8px;\n"
"opacity: 200;\n"
"")
        self.pushButtonRegister.setAutoDefault(False)
        self.pushButtonRegister.setDefault(False)
        self.pushButtonRegister.setFlat(False)
        self.pushButtonRegister.setObjectName("pushButtonRegister")
        self.pushButtonCancel = QPushButton(Form)
        self.pushButtonCancel.setGeometry(QRect(59, 423, 500, 48))
        self.pushButtonCancel.setMinimumSize(QSize(0, 45))
        self.pushButtonCancel.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 17pt \"Verdana\";\n"
"border: 2px solid rgb(79,159,238);\n"
"padding: 5px;\n"
"border-radius: 8px;\n"
"opacity: 200;\n"
"")
        self.pushButtonCancel.setDefault(False)
        self.pushButtonCancel.setFlat(False)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.lineEditPasswd = QLineEdit(Form)
        self.lineEditPasswd.setGeometry(QRect(204, 102, 355, 40))
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
        self.lineEditPasswd.setEchoMode(QLineEdit.Password)
        self.lineEditPasswd.setObjectName("lineEditPasswd")
        self.lineEditAccount = QLineEdit(Form)
        self.lineEditAccount.setGeometry(QRect(204, 43, 355, 40))
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
        self.label_2 = QLabel(Form)
        self.label_2.setGeometry(QRect(115, 43, 83, 44))
        self.label_2.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 17pt \"Verdana\";\n"
"padding: 5px;\n"
"border-radius: 8px;\n"
"opacity: 200;")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.pushButtonClose = QPushButton(Form)
        self.pushButtonClose.setGeometry(QRect(577, 8, 35, 25))
        self.pushButtonClose.setMinimumSize(QSize(35, 25))
        self.pushButtonClose.setMaximumSize(QSize(35, 25))
        self.pushButtonClose.setStyleSheet("color: white;\n"
"font: 12pt \"Arial\";")
        self.pushButtonClose.setFlat(True)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.pushButtonVerify = QPushButton(Form)
        self.pushButtonVerify.setGeometry(QRect(96, 280, 98, 48))
        self.pushButtonVerify.setMinimumSize(QSize(0, 45))
        font = QFont()
        font.setFamily("Verdana")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QFont.Weight(50))
        self.pushButtonVerify.setFont(font)
        self.pushButtonVerify.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 17pt \"Verdana\";\n"
"border: 2px solid rgb(79,159,238);\n"
"padding: 5px;\n"
"border-radius: 8px;\n"
"opacity: 200;")
        self.pushButtonVerify.setObjectName("pushButtonVerify")
        self.lineEditPhone = QLineEdit(Form)
        self.lineEditPhone.setGeometry(QRect(200, 220, 355, 40))
        self.lineEditPhone.setMinimumSize(QSize(0, 40))
        self.lineEditPhone.setStyleSheet("QLineEdit {\n"
"      color: rgb(220,225,236);\n"
"      font: 15pt \"Verdana\";\n"
"      border: None;\n"
"      border-bottom-color: white;\n"
"      border-radius: 8px;\n"
"      padding: 0 8px;\n"
"      background: rgb(52,59,72);\n"
"      selection-background-color: darkgray;\n"
"}")
        self.lineEditPhone.setObjectName("lineEditPhone")
        self.label_5 = QLabel(Form)
        self.label_5.setGeometry(QRect(55, 220, 139, 44))
        self.label_5.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 17pt \"Verdana\";\n"
"padding: 5px;\n"
"border-radius: 8px;\n"
"opacity: 200;")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEditAccount, self.lineEditPasswd)
        Form.setTabOrder(self.lineEditPasswd, self.lineEditPasswd_2)
        Form.setTabOrder(self.lineEditPasswd_2, self.lineEditPhone)
        Form.setTabOrder(self.lineEditPhone, self.lineEditVerify)
        Form.setTabOrder(self.lineEditVerify, self.pushButtonVerify)
        Form.setTabOrder(self.pushButtonVerify, self.pushButtonRegister)
        Form.setTabOrder(self.pushButtonRegister, self.pushButtonCancel)
        Form.setTabOrder(self.pushButtonCancel, self.pushButtonClose)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "??????"))
        self.label_3.setText(_translate("Form", "??????"))
        self.label_4.setText(_translate("Form", "????????????"))
        self.pushButtonRegister.setText(_translate("Form", "??????"))
        self.pushButtonCancel.setText(_translate("Form", "??????"))
        self.label_2.setText(_translate("Form", "??????"))
        self.pushButtonClose.setText(_translate("Form", "X"))
        self.pushButtonVerify.setText(_translate("Form", "?????????"))
        self.label_5.setText(_translate("Form", "????????????"))
