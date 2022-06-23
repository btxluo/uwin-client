# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_verify_code.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from modern_gui.qt_core import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(Qt.ApplicationModal)
        Form.resize(505, 205)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setGeometry(QRect(20, 70, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.codeImageLabel = QLabel(Form)
        self.codeImageLabel.setGeometry(QRect(190, 60, 181, 41))
        self.codeImageLabel.setText("")
        self.codeImageLabel.setScaledContents(True)
        self.codeImageLabel.setObjectName("codeImageLabel")
        self.confirmPushButton = QPushButton(Form)
        self.confirmPushButton.setGeometry(QRect(150, 140, 92, 28))
        self.confirmPushButton.setObjectName("confirmPushButton")
        self.refreshPushButton = QPushButton(Form)
        self.refreshPushButton.setGeometry(QRect(390, 70, 51, 41))
        self.refreshPushButton.setObjectName("refreshPushButton")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "请输入验证码"))
        self.codeImageLabel.setToolTip(_translate("Form", "看不清？点击刷新"))
        self.confirmPushButton.setText(_translate("Form", "确定"))
        self.refreshPushButton.setText(_translate("Form", "刷新"))
