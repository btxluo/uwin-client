import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from login_form import Ui_Form


class LoginWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet(
            """
            QPushButton {
                border-style: outset;
                border-radius: 0px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #4f9fee;
                border-style: inset;
            }
            QPushButton:pressed {
                background-color: #87bdf3;
                border-style: inset;
            }
            """
        )
        self.setWindowIcon(QIcon(":/icons/icons/uwin_dot_bright-256x256.png"))
        if sys.platform.startswith('win'):
            import ctypes
            # Make sure Pyinstaller icons are still grouped
            if not sys.argv[0].endswith('.exe'):
                ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'uwin')  # Arbitrary string
        self.pushButton_3.clicked.connect(self.close)
        self.line.setVisible(False)
        self.line_2.setVisible(False)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # h = QtWidgets.QHBoxLayout()
        #
        # w = ColorQLineEdit("one")
        # h.addWidget(w)
        #
        # w = ColorQLineEdit("two")
        # h.addWidget(w)
        #
        # self.setLayout(h)


# class ColorQLineEdit(QtWidgets.QLineEdit):
#     def focusInEvent(self, event):
#         print("in")
#         self.setStyleSheet("background-color: yellow; color: red;")
#         super().focusInEvent(event)
#
#     def focusOutEvent(self, event):
#         print("out")
#         self.setStyleSheet("background-color: white; color: black;")
#         super().focusOutEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    win.show()
    # time.sleep(2)

    # win.show_picture(win.codeImageLabel)
    # win.show_picture(win.registerCodeImageLabel)
    sys.exit(app.exec_())
