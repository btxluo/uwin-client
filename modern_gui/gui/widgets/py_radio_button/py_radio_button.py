# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from modern_gui.qt_core import *

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QRadioButton {{
	border: none;
    padding-left: 10px;
    padding-right: 10px;
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
}}
QRadioButton:hover {{
	background-color: {_bg_color_hover};
}}
QRadioButton:pressed {{	
	background-color: {_bg_color_pressed};
}}
QRadioButton::indicator{{
	width:11px;
	height:11px;
	border-radius:6px;
	border-style: solid;
	border-width: 1px;
	border-color: #ffffff;
}}
QRadioButton::indicator:checked {{
	background-color:green;
}}
QRadioButton::indicator:unchecked {{
	background-color:rgb(255, 255, 255);
}}
'''


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyRadioButton(QRadioButton):
    def __init__(
            self,
            text,
            radius,
            color,
            bg_color,
            bg_color_hover,
            bg_color_pressed,
            parent=None,
    ):
        super().__init__()

        # SET PARAMETRES
        self.setText(text)
        if parent != None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        # SET STYLESHEET
        custom_style = style.format(
            _color=color,
            _radius=radius,
            _bg_color=bg_color,
            _bg_color_hover=bg_color_hover,
            _bg_color_pressed=bg_color_pressed
        )
        self.setStyleSheet(custom_style)
