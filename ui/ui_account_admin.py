# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_account_admin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(515, 484)
        Form.setAutoFillBackground(False)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 501, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.tabAccount = QtWidgets.QWidget()
        self.tabAccount.setObjectName("tabAccount")
        self.localVerifyLineEdit = QtWidgets.QLineEdit(self.tabAccount)
        self.localVerifyLineEdit.setGeometry(QtCore.QRect(40, 30, 181, 31))
        self.localVerifyLineEdit.setObjectName("localVerifyLineEdit")
        self.codeImageLabel_2 = QtWidgets.QLabel(self.tabAccount)
        self.codeImageLabel_2.setGeometry(QtCore.QRect(240, 20, 191, 41))
        self.codeImageLabel_2.setText("")
        self.codeImageLabel_2.setScaledContents(True)
        self.codeImageLabel_2.setObjectName("codeImageLabel_2")
        self.sendPushButton = QtWidgets.QPushButton(self.tabAccount)
        self.sendPushButton.setGeometry(QtCore.QRect(40, 80, 391, 31))
        self.sendPushButton.setObjectName("sendPushButton")
        self.verifyLineEdit = QtWidgets.QLineEdit(self.tabAccount)
        self.verifyLineEdit.setGeometry(QtCore.QRect(40, 130, 391, 31))
        self.verifyLineEdit.setObjectName("verifyLineEdit")
        self.accountLineEdit = QtWidgets.QLineEdit(self.tabAccount)
        self.accountLineEdit.setGeometry(QtCore.QRect(40, 180, 391, 31))
        self.accountLineEdit.setObjectName("accountLineEdit")
        self.pwdLineEdit = QtWidgets.QLineEdit(self.tabAccount)
        self.pwdLineEdit.setGeometry(QtCore.QRect(40, 230, 391, 31))
        self.pwdLineEdit.setObjectName("pwdLineEdit")
        self.pwdConfirmLineEdit = QtWidgets.QLineEdit(self.tabAccount)
        self.pwdConfirmLineEdit.setGeometry(QtCore.QRect(40, 280, 391, 31))
        self.pwdConfirmLineEdit.setObjectName("pwdConfirmLineEdit")
        self.nickLineEdit = QtWidgets.QLineEdit(self.tabAccount)
        self.nickLineEdit.setGeometry(QtCore.QRect(40, 330, 391, 31))
        self.nickLineEdit.setObjectName("nickLineEdit")
        self.tabWidget.addTab(self.tabAccount, "")
        self.tabPasswd = QtWidgets.QWidget()
        self.tabPasswd.setObjectName("tabPasswd")
        self.codeImageLabel_3 = QtWidgets.QLabel(self.tabPasswd)
        self.codeImageLabel_3.setGeometry(QtCore.QRect(250, 50, 191, 41))
        self.codeImageLabel_3.setText("")
        self.codeImageLabel_3.setScaledContents(True)
        self.codeImageLabel_3.setObjectName("codeImageLabel_3")
        self.verifyLineEdit_2 = QtWidgets.QLineEdit(self.tabPasswd)
        self.verifyLineEdit_2.setGeometry(QtCore.QRect(50, 160, 391, 31))
        self.verifyLineEdit_2.setObjectName("verifyLineEdit_2")
        self.sendPushButton_2 = QtWidgets.QPushButton(self.tabPasswd)
        self.sendPushButton_2.setGeometry(QtCore.QRect(50, 110, 391, 31))
        self.sendPushButton_2.setObjectName("sendPushButton_2")
        self.localVerifyLineEdit_2 = QtWidgets.QLineEdit(self.tabPasswd)
        self.localVerifyLineEdit_2.setGeometry(QtCore.QRect(50, 60, 181, 31))
        self.localVerifyLineEdit_2.setObjectName("localVerifyLineEdit_2")
        self.pwdLineEdit_2 = QtWidgets.QLineEdit(self.tabPasswd)
        self.pwdLineEdit_2.setGeometry(QtCore.QRect(50, 210, 391, 31))
        self.pwdLineEdit_2.setObjectName("pwdLineEdit_2")
        self.pwdConfirmLineEdit_2 = QtWidgets.QLineEdit(self.tabPasswd)
        self.pwdConfirmLineEdit_2.setGeometry(QtCore.QRect(50, 260, 391, 31))
        self.pwdConfirmLineEdit_2.setObjectName("pwdConfirmLineEdit_2")
        self.tabWidget.addTab(self.tabPasswd, "")
        self.tabNick = QtWidgets.QWidget()
        self.tabNick.setObjectName("tabNick")
        self.lineEdit = QtWidgets.QLineEdit(self.tabNick)
        self.lineEdit.setGeometry(QtCore.QRect(60, 140, 381, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tabNick, "")
        self.tabAccInfo = QtWidgets.QWidget()
        self.tabAccInfo.setObjectName("tabAccInfo")
        self.label = QtWidgets.QLabel(self.tabAccInfo)
        self.label.setGeometry(QtCore.QRect(80, 80, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tabAccInfo)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 81, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tabAccInfo)
        self.label_3.setGeometry(QtCore.QRect(80, 210, 81, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tabAccInfo)
        self.label_4.setGeometry(QtCore.QRect(80, 270, 81, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tabAccInfo)
        self.label_5.setGeometry(QtCore.QRect(160, 80, 151, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tabAccInfo)
        self.label_6.setGeometry(QtCore.QRect(160, 140, 151, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tabAccInfo)
        self.label_7.setGeometry(QtCore.QRect(150, 200, 151, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tabAccInfo)
        self.label_8.setGeometry(QtCore.QRect(150, 270, 151, 31))
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tabAccInfo, "")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 420, 92, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 420, 92, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.localVerifyLineEdit.setPlaceholderText(_translate("Form", "请输入图片验证码"))
        self.codeImageLabel_2.setToolTip(_translate("Form", "看不清？点击刷新"))
        self.sendPushButton.setText(_translate("Form", "免费获取验证码"))
        self.verifyLineEdit.setPlaceholderText(_translate("Form", "请输入短信验证码"))
        self.accountLineEdit.setPlaceholderText(_translate("Form", "设置账号，只能设置一次"))
        self.pwdLineEdit.setPlaceholderText(_translate("Form", "请输入密码"))
        self.pwdConfirmLineEdit.setPlaceholderText(_translate("Form", "请再次确认密码"))
        self.nickLineEdit.setPlaceholderText(_translate("Form", "请输入昵称"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAccount), _translate("Form", "设置账户"))
        self.codeImageLabel_3.setToolTip(_translate("Form", "看不清？点击刷新"))
        self.verifyLineEdit_2.setPlaceholderText(_translate("Form", "请输入短信验证码"))
        self.sendPushButton_2.setText(_translate("Form", "免费获取验证码"))
        self.localVerifyLineEdit_2.setPlaceholderText(_translate("Form", "请输入图片验证码"))
        self.pwdLineEdit_2.setPlaceholderText(_translate("Form", "请输入密码"))
        self.pwdConfirmLineEdit_2.setPlaceholderText(_translate("Form", "请再次确认密码"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPasswd), _translate("Form", "修改密码"))
        self.lineEdit.setPlaceholderText(_translate("Form", "请输入新昵称"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNick), _translate("Form", "修改昵称"))
        self.label.setText(_translate("Form", "账户名"))
        self.label_2.setText(_translate("Form", "手机号"))
        self.label_3.setText(_translate("Form", "昵称"))
        self.label_4.setText(_translate("Form", "VIP"))
        self.label_5.setText(_translate("Form", "TextLabel"))
        self.label_6.setText(_translate("Form", "TextLabel"))
        self.label_7.setText(_translate("Form", "TextLabel"))
        self.label_8.setText(_translate("Form", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAccInfo), _translate("Form", "账户详情"))
        self.pushButton.setText(_translate("Form", "确认"))
        self.pushButton_2.setText(_translate("Form", "退出"))