# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Uproject\new-uwin\modern_login\login_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from modern_gui.qt_core import *
import modern_login.icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(437, 523)
        Form.setStyleSheet("")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QWidget(Form)
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.widget.setStyleSheet(".QWidget{background-color: rgb(44,49,60);\n"
"border-radius: 8px;\n"
"border: 2px solid #343b48;}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(9, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QSize(35, 25))
        self.pushButton_3.setMaximumSize(QSize(35, 25))
        self.pushButton_3.setStyleSheet("color: white;\n"
"font: 12pt \"Arial\";\n"
"")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3, 0, Qt.AlignRight)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QLabel(self.widget)
        self.label.setMinimumSize(QSize(128, 75))
        self.label.setMaximumSize(QSize(128, 75))
        self.label.setStyleSheet("image: url(:/icons/icons/uwin_dot_h-256x256.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setContentsMargins(50, 35, 59, -1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QLabel(self.widget)
        self.label_4.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 15pt \"Verdana\";")
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)
        self.lineEditAccount = QLineEdit(self.widget)
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
        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEditAccount)
        self.line = QFrame(self.widget)
        self.line.setEnabled(True)
        self.line.setStyleSheet("border: 2px solid rgb(79,159,238);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.line)
        self.label_3 = QLabel(self.widget)
        self.label_3.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 15pt \"Verdana\";")
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)
        self.lineEditPasswd = QLineEdit(self.widget)
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
        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEditPasswd)
        self.line_2 = QFrame(self.widget)
        self.line_2.setStyleSheet("border: 2px solid rgb(79,159,238);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout_2.setWidget(4, QFormLayout.SpanningRole, self.line_2)
        self.pushButtonLogin = QPushButton(self.widget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonLogin.sizePolicy().hasHeightForWidth())
        self.pushButtonLogin.setSizePolicy(sizePolicy)
        self.pushButtonLogin.setMinimumSize(QSize(0, 45))
        font = QFont()
        font.setFamily("Verdana")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QFont.Weight(50))
        font.setKerning(True)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setAutoFillBackground(False)
        self.pushButtonLogin.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 17pt \"Verdana\";\n"
"border: 2px solid rgb(79,159,238);\n"
"padding: 5px;\n"
"border-radius: 8px;\n"
"opacity: 200;\n"
"")
        self.pushButtonLogin.setAutoDefault(False)
        self.pushButtonLogin.setDefault(False)
        self.pushButtonLogin.setFlat(False)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.formLayout_2.setWidget(5, QFormLayout.SpanningRole, self.pushButtonLogin)
        self.pushButtonRegister = QPushButton(self.widget)
        self.pushButtonRegister.setMinimumSize(QSize(0, 45))
        self.pushButtonRegister.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 17pt \"Verdana\";\n"
"border: 2px solid rgb(79,159,238);\n"
"padding: 5px;\n"
"border-radius: 8px;\n"
"opacity: 200;\n"
"")
        self.pushButtonRegister.setDefault(False)
        self.pushButtonRegister.setFlat(False)
        self.pushButtonRegister.setObjectName("pushButtonRegister")
        self.formLayout_2.setWidget(6, QFormLayout.SpanningRole, self.pushButtonRegister)
        self.pushButtonForgetPasswd = QPushButton(self.widget)
        self.pushButtonForgetPasswd.setMinimumSize(QSize(0, 45))
        font = QFont()
        font.setFamily("Verdana")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QFont.Weight(50))
        self.pushButtonForgetPasswd.setFont(font)
        self.pushButtonForgetPasswd.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 17pt \"Verdana\";\n"
"border: 2px solid rgb(79,159,238);\n"
"padding: 5px;\n"
"border-radius: 8px;\n"
"opacity: 200;")
        self.pushButtonForgetPasswd.setObjectName("pushButtonForgetPasswd")
        self.formLayout_2.setWidget(7, QFormLayout.SpanningRole, self.pushButtonForgetPasswd)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.formLayout_2.setItem(8, QFormLayout.SpanningRole, spacerItem)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.formLayout_2.setItem(3, QFormLayout.SpanningRole, spacerItem1)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.addWidget(self.widget)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.pushButton_3.setText(_translate("Form", "X"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><img src=\":/icons/icons/user_32x32.png\"/></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><img src=\":/icons/icons/lock_32x32.png\"/></p></body></html>"))
        self.pushButtonLogin.setText(_translate("Form", "登录"))
        self.pushButtonRegister.setText(_translate("Form", "注册"))
        self.pushButtonForgetPasswd.setText(_translate("Form", "重置密码"))
