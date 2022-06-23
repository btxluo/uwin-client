from client import LoginWindow
from modern_gui.qt_core import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    win.show()
    # time.sleep(2)

    # win.show_picture(win.codeImageLabel)
    # win.show_picture(win.registerCodeImageLabel)
    sys.exit(app.exec_())