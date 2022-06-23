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

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
# from modern_gui.gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from modern_gui.gui.widgets.py_label import PyLabel
from modern_gui.gui.widgets.py_table_view.py_table_view import PyTableView

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from modern_gui.qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from modern_gui.gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from modern_gui.gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from modern_gui.gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from .functions_main_window import MainFunctions
from .ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from .functions_main_window import *


# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon": "icon_home.svg",
            "btn_id": "btn_home",
            "btn_text": "首页",
            "btn_tooltip": "首页",
            "show_top": True,
            "is_active": True
        },
        {
            "btn_icon": "ai.svg",
            "btn_id": "btn_widgets",
            "btn_text": "AI决策",
            "btn_tooltip": "AI决策",
            "show_top": True,
            "is_active": False
        },
        # {
        #     "btn_icon": "icon_add_user.svg",
        #     "btn_id": "btn_add_user",
        #     "btn_text": "Add Users",
        #     "btn_tooltip": "Add users",
        #     "show_top": True,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "icon_file.svg",
        #     "btn_id": "btn_new_file",
        #     "btn_text": "New File",
        #     "btn_tooltip": "Create new file",
        #     "show_top": True,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "icon_folder_open.svg",
        #     "btn_id": "btn_open_file",
        #     "btn_text": "Open File",
        #     "btn_tooltip": "Open file",
        #     "show_top": True,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "icon_save.svg",
        #     "btn_id": "btn_save",
        #     "btn_text": "Save File",
        #     "btn_tooltip": "Save file",
        #     "show_top": True,
        #     "is_active": False
        # },
        {
            "btn_icon": "icon_info.svg",
            "btn_id": "btn_info",
            "btn_text": "帮助",
            "btn_tooltip": "帮助",
            "show_top": False,
            "is_active": False
        },
        {
            "btn_icon": "icon_user.svg",
            "btn_id": "btn_settings",
            "btn_text": "VIP 管理",
            "btn_tooltip": "VIP 管理",
            "show_top": False,
            "is_active": False
        }
    ]

    # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    # add_title_bar_menus = [
    #     {
    #         "btn_icon": "icon_search.svg",
    #         "btn_id": "btn_search",
    #         "btn_tooltip": "Search",
    #         "is_active": False
    #     },
    #     {
    #         "btn_icon": "icon_settings.svg",
    #         "btn_id": "btn_top_settings",
    #         "btn_tooltip": "Top settings",
    #         "is_active": False
    #     }
    # ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self, res, vip_info):
        if len(res) == 0:
            res = [
                {'name': '一个月', 'price': 38800},
                {'name': '三个月', 'price': 88800},
                {'name': '半年', 'price': 128800},
            ]
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])

        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        # self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("欢迎进入UWIN - AI决策系统\n声明：本软件只作研究使用，请遵纪守法，勿将其用于非法行为")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu=self.ui.left_column.menus.menu_1,
            title="Vip 管理",
            icon_path=Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # LEFT COLUMN
        # ///////////////////////////////////////////////////////////////

        # MODIFY PASSWORD BTN
        self.modify_password_btn = PyPushButton(
            text="修改密码",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.modify_password_btn.setMaximumHeight(40)
        self.ui.left_column.menus.btn_1_layout.addWidget(self.modify_password_btn)
        # 修改密码
        self.modify_password_btn.clicked.connect(self.modify_password_clicked)

        # BTN 1
        self.left_btn_1 = PyPushButton(
            text="充值",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.left_btn_1.setMaximumHeight(40)
        self.ui.left_column.menus.btn_1_layout.addWidget(self.left_btn_1)
        # get vip
        self.left_btn_1.clicked.connect(self.btn1_clicked)

        # BTN 2
        # self.left_btn_2 = PyPushButton(
        #     text="Btn With Icon",
        #     radius=8,
        #     color=self.themes["app_color"]["text_foreground"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["dark_four"]
        # )
        # self.icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        # self.left_btn_2.setIcon(self.icon)
        # self.left_btn_2.setMaximumHeight(40)
        # self.ui.left_column.menus.btn_2_layout.addWidget(self.left_btn_2)

        self.left_radio_btn_weixin = PyRadioButton(
            text="微信",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.left_radio_btn_weixin.setMaximumHeight(20)
        self.ui.left_column.menus.btn_2_layout.addWidget(self.left_radio_btn_weixin)

        self.left_radio_btn_alipay = PyRadioButton(
            text="支付宝",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.left_radio_btn_alipay.setMaximumHeight(20)
        # self.left_radio_btn_alipay.setDisabled(True)
        self.left_radio_btn_alipay.setChecked(True)
        self.ui.left_column.menus.btn_2_layout.addWidget(self.left_radio_btn_alipay)

        # PyRadio
        self.order_btns = []
        for order in res:
            radio_btn = PyRadioButton(
                text=f"%s(￥%d)" % (order['name'], order['price']/100),
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_one"],
                bg_color_hover=self.themes["app_color"]["dark_three"],
                bg_color_pressed=self.themes["app_color"]["dark_four"]
            )
            radio_btn.setMaximumHeight(20)
            self.ui.left_column.menus.radio_btn_layout.addWidget(radio_btn)
            self.order_btns.append([radio_btn, order['name']])
        self.ui.left_column.menus.label_vip_date.setText(vip_info)
        # # PyRadio
        # self.left_radio_btn2 = PyRadioButton(
        #     text="三个月(888)",
        #     radius=8,
        #     color=self.themes["app_color"]["text_foreground"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["dark_four"]
        # )
        # self.left_radio_btn2.setMaximumHeight(20)
        # self.left_radio_btn2.setChecked(True)
        # self.ui.left_column.menus.radio_btn_layout.addWidget(self.left_radio_btn2)
        #
        # # PyRadio
        # self.left_radio_btn3 = PyRadioButton(
        #     text="半年(1288)",
        #     radius=8,
        #     color=self.themes["app_color"]["text_foreground"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["dark_four"]
        # )
        # self.left_radio_btn3.setMaximumHeight(20)
        # self.ui.left_column.menus.radio_btn_layout.addWidget(self.left_radio_btn3)

        # PAGES
        # ///////////////////////////////////////////////////////////////

        # PAGE 1 - ADD LOGO TO MAIN PAGE
        self.logo_svg = QSvgWidget(Functions.set_svg_image("uwin_dot_h-150x48.svg"))
        self.ui.load_pages.logo_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)

        # PAGE 2
        # CIRCULAR PROGRESS 1
        self.circular_progress_1 = PyCircularProgress(
            value=80,
            progress_color=self.themes["app_color"]["context_color"],
            text_color=self.themes["app_color"]["text_title"],
            font_size=14,
            bg_color=self.themes["app_color"]["dark_four"]
        )
        self.circular_progress_1.setFixedSize(200, 200)

        # CIRCULAR PROGRESS 2
        self.circular_progress_2 = PyCircularProgress(
            value=45,
            progress_width=4,
            progress_color=self.themes["app_color"]["context_color"],
            text_color=self.themes["app_color"]["context_color"],
            font_size=14,
            bg_color=self.themes["app_color"]["bg_three"]
        )
        self.circular_progress_2.setFixedSize(160, 160)

        # CIRCULAR PROGRESS 3
        self.circular_progress_3 = PyCircularProgress(
            value=75,
            progress_width=2,
            progress_color=self.themes["app_color"]["pink"],
            text_color=self.themes["app_color"]["white"],
            font_size=14,
            bg_color=self.themes["app_color"]["bg_three"]
        )
        self.circular_progress_3.setFixedSize(140, 140)

        # # PY SLIDER 1
        # self.vertical_slider_1 = PySlider(
        #     margin=8,
        #     bg_size=10,
        #     bg_radius=5,
        #     handle_margin=-3,
        #     handle_size=16,
        #     handle_radius=8,
        #     bg_color=self.themes["app_color"]["dark_three"],
        #     bg_color_hover=self.themes["app_color"]["dark_four"],
        #     handle_color=self.themes["app_color"]["context_color"],
        #     handle_color_hover=self.themes["app_color"]["context_hover"],
        #     handle_color_pressed=self.themes["app_color"]["context_pressed"]
        # )
        # self.vertical_slider_1.setMinimumHeight(100)

        # # PY SLIDER 2
        # self.vertical_slider_2 = PySlider(
        #     bg_color=self.themes["app_color"]["dark_three"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     handle_color=self.themes["app_color"]["context_color"],
        #     handle_color_hover=self.themes["app_color"]["context_hover"],
        #     handle_color_pressed=self.themes["app_color"]["context_pressed"]
        # )
        # self.vertical_slider_2.setMinimumHeight(100)

        # PY SLIDER 3
        self.vertical_slider_3 = PySlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_four"],
            handle_color=self.themes["app_color"]["context_color"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_3.setOrientation(Qt.Horizontal)
        self.vertical_slider_3.setMaximumWidth(200)

        # # PY SLIDER 4
        # self.vertical_slider_4 = PySlider(
        #     bg_color=self.themes["app_color"]["dark_three"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     handle_color=self.themes["app_color"]["context_color"],
        #     handle_color_hover=self.themes["app_color"]["context_hover"],
        #     handle_color_pressed=self.themes["app_color"]["context_pressed"]
        # )
        # self.vertical_slider_4.setOrientation(Qt.Horizontal)
        # self.vertical_slider_4.setMaximumWidth(200)

        # # ICON BUTTON 1
        # self.icon_button_1 = PyIconButton(
        #     icon_path=Functions.set_svg_icon("icon_heart.svg"),
        #     parent=self,
        #     app_parent=self.ui.central_widget,
        #     tooltip_text="Icon button - Heart",
        #     width=40,
        #     height=40,
        #     radius=20,
        #     dark_one=self.themes["app_color"]["dark_one"],
        #     icon_color=self.themes["app_color"]["icon_color"],
        #     icon_color_hover=self.themes["app_color"]["icon_hover"],
        #     icon_color_pressed=self.themes["app_color"]["icon_active"],
        #     icon_color_active=self.themes["app_color"]["icon_active"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["pink"]
        # )
        #
        # # ICON BUTTON 2
        # self.icon_button_2 = PyIconButton(
        #     icon_path=Functions.set_svg_icon("icon_add_user.svg"),
        #     parent=self,
        #     app_parent=self.ui.central_widget,
        #     tooltip_text="BTN with tooltip",
        #     width=40,
        #     height=40,
        #     radius=8,
        #     dark_one=self.themes["app_color"]["dark_one"],
        #     icon_color=self.themes["app_color"]["icon_color"],
        #     icon_color_hover=self.themes["app_color"]["icon_hover"],
        #     icon_color_pressed=self.themes["app_color"]["white"],
        #     icon_color_active=self.themes["app_color"]["icon_active"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["green"],
        # )
        #
        # # ICON BUTTON 3
        # self.icon_button_3 = PyIconButton(
        #     icon_path=Functions.set_svg_icon("icon_add_user.svg"),
        #     parent=self,
        #     app_parent=self.ui.central_widget,
        #     tooltip_text="BTN actived! (is_actived = True)",
        #     width=40,
        #     height=40,
        #     radius=8,
        #     dark_one=self.themes["app_color"]["dark_one"],
        #     icon_color=self.themes["app_color"]["icon_color"],
        #     icon_color_hover=self.themes["app_color"]["icon_hover"],
        #     icon_color_pressed=self.themes["app_color"]["white"],
        #     icon_color_active=self.themes["app_color"]["icon_active"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["context_color"],
        #     is_active=True
        # )

        # PY LINE EDIT
        self.label_1 = QLabel()
        self.label_1.setMinimumHeight(30)
        self.label_1.setMaximumWidth(30)
        self.label_1.setPixmap(
            QPixmap(Functions.set_image("money_1.png")).scaled(QSize(28, 28), Qt.KeepAspectRatio))
        self.line_edit_1 = PyLabel(
            text="",
            place_holder_text="Place holder text",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        # self.line_edit_1.setReadOnly(True)
        self.line_edit_1.setMinimumHeight(30)

        # PY LINE EDIT
        self.label_2 = QLabel()
        self.label_2.setMinimumHeight(30)
        self.label_2.setMaximumWidth(30)
        self.label_2.setPixmap(QPixmap(Functions.set_image("instruction.png")).scaled(QSize(30, 30), Qt.KeepAspectRatio))
        self.line_edit_2 = PyLabel(
            text="",
            place_holder_text="Place holder text",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        # self.line_edit_2.setReadOnly(True)
        self.line_edit_2.setMinimumHeight(30)

        # PY LINE EDIT
        self.label_3 = QLabel()
        self.label_3.setMinimumHeight(30)
        self.label_3.setMaximumWidth(30)
        self.label_3.setPixmap(QPixmap(Functions.set_image("bet.png")).scaled(QSize(30, 30), Qt.KeepAspectRatio))
        # self.line_edit_3 = PyLineEdit(
        #     text="",
        #     place_holder_text="Place holder text",
        #     radius=8,
        #     border_size=2,
        #     color=self.themes["app_color"]["text_foreground"],
        #     selection_color=self.themes["app_color"]["white"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_active=self.themes["app_color"]["dark_three"],
        #     context_color=self.themes["app_color"]["context_color"]
        # )
        # self.line_edit_3.setReadOnly(True)
        # self.line_edit_3.setMinimumHeight(30)
        self.tip_label_3 = PyLabel(
            text="",
            place_holder_text="Place holder text",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.tip_label_3.setMinimumHeight(30)
        # self.tip_label_3.setMinimumWidth(120)

        # PUSH BUTTON 1
        self.push_button_1 = PyPushButton(
            text="",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            # bg_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["blue"],
            bg_color_hover=self.themes["app_color"]["blue_two"],
            bg_color_pressed=self.themes["app_color"]["blue_three"]
        )
        self.icon_1 = QIcon(Functions.set_image("man.png"))
        self.push_button_1.setMinimumHeight(40)
        self.push_button_1.setIcon(self.icon_1)

        # PUSH BUTTON 2
        self.push_button_2 = PyPushButton(
            text="",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            # bg_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["red"],
            bg_color_hover=self.themes["app_color"]["red_two"],
            bg_color_pressed=self.themes["app_color"]["red_three"]
        )
        self.icon_2 = QIcon(Functions.set_image("woman.png"))
        self.push_button_2.setMinimumHeight(40)
        self.push_button_2.setIcon(self.icon_2)

        # PY LINE EDIT
        self.line_edit = PyLineEdit(
            text="",
            place_holder_text="示例：010101",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit.setMinimumHeight(30)
        # 只能输入0,1
        my_regex = QRegularExpression(r"^[01]*$")
        my_validator = QRegularExpressionValidator(my_regex, self.line_edit)
        self.line_edit.setValidator(my_validator)

        # TOGGLE BUTTON
        self.toggle_button = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"]
        )

        # TABLE VIEWS
        self.table_view = PyTableView(
            radius=8,
            border_radius=0,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            # bottom_line_color=self.themes["app_color"]["bg_three"],
            # grid_line_color=self.themes["app_color"]["bg_one"] + " transparent",
            bottom_line_color="transparent",
            grid_line_color="transparent",
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.table_view.horizontalHeader().setDefaultSectionSize(20)
        self.table_view.verticalHeader().setDefaultSectionSize(20)
        self.table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_view.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_view.horizontalHeader().setVisible(False)
        self.table_view.verticalHeader().setVisible(False)

        # ICON BUTTON 2
        self.icon_button_2 = PyIconButton(
            icon_path=Functions.set_svg_icon("return_icon.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="决策",
            width=30,
            height=30,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )

        # ICON BUTTON 3
        self.icon_button_3 = PyIconButton(
            icon_path=Functions.set_svg_icon("refresh_icon.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="重新开局",
            width=30,
            height=30,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        # self.icon_3 = QIcon(Functions.set_svg_icon("refresh_icon.svg"))
        # self.icon_button_3.setMinimumHeight(30)
        # self.icon_button_3.setIcon(self.icon_3)
        # self.push_button_3 = PyPushButton(
        #     text="",
        #     radius=8,
        #     color=self.themes["app_color"]["text_foreground"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     # bg_color=self.themes["app_color"]["red"],
        #     bg_color_hover=self.themes["app_color"]["dark_two"],
        #     bg_color_pressed=self.themes["app_color"]["dark_three"]
        # )
        # self.icon_3 = QIcon(Functions.set_svg_icon("refresh_icon.svg"))
        # self.push_button_3.setMinimumHeight(30)
        # self.push_button_3.setIcon(self.icon_3)
        # self.push_button_3.setToolTip("重新开局")
        # self.table_view.setShowGrid(False)
        # self.table_widget.setColumnCount(60)
        # self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        #
        # # Columns / Header
        # self.column_1 = QTableWidgetItem()
        # self.column_1.setTextAlignment(Qt.AlignCenter)
        # self.column_1.setText("NAME")
        #
        # self.column_2 = QTableWidgetItem()
        # self.column_2.setTextAlignment(Qt.AlignCenter)
        # self.column_2.setText("NICK")
        #
        # self.column_3 = QTableWidgetItem()
        # self.column_3.setTextAlignment(Qt.AlignCenter)
        # self.column_3.setText("PASS")
        #
        # # Set column
        # self.table_widget.setHorizontalHeaderItem(0, self.column_1)
        # self.table_widget.setHorizontalHeaderItem(1, self.column_2)
        # self.table_widget.setHorizontalHeaderItem(2, self.column_3)
        #
        # for x in range(10):
        #     row_number = self.table_widget.rowCount()
        #     self.table_widget.insertRow(row_number)  # Insert row
        #     self.table_widget.setItem(row_number, 0, QTableWidgetItem(str("Wanderson")))  # Add name
        #     self.table_widget.setItem(row_number, 1, QTableWidgetItem(str("vfx_on_fire_" + str(x))))  # Add nick
        #     self.pass_text = QTableWidgetItem()
        #     self.pass_text.setTextAlignment(Qt.AlignCenter)
        #     self.pass_text.setText("12345" + str(x))
        #     self.table_widget.setItem(row_number, 2, self.pass_text)  # Add pass
        #     self.table_widget.setRowHeight(row_number, 22)

        # ADD WIDGETS
        self.ui.load_pages.row_1_layout.addWidget(self.table_view)
        # self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_1)
        # self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_2)
        # self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_3)
        # self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_1)
        # self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_2)
        self.ui.load_pages.row_2_layout.addWidget(self.label_1)
        self.ui.load_pages.row_2_layout.addWidget(self.line_edit_1)
        self.ui.load_pages.row_2_layout.addWidget(self.label_2)
        self.ui.load_pages.row_2_layout.addWidget(self.tip_label_3)
        self.ui.load_pages.row_2_layout.addWidget(self.label_3)
        self.ui.load_pages.row_2_layout.addWidget(self.line_edit_2)
        self.ui.load_pages.row_3_layout.addWidget(self.vertical_slider_3)
        # self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_4)
        # self.ui.load_pages.row_3_layout.addWidget(self.icon_button_1)
        # self.ui.load_pages.row_3_layout.addWidget(self.icon_button_2)
        # self.ui.load_pages.row_3_layout.addWidget(self.icon_button_3)
        self.ui.load_pages.row_3_layout.addWidget(self.push_button_1)
        self.ui.load_pages.row_3_layout.addWidget(self.push_button_2)
        self.ui.load_pages.row_3_layout.addWidget(self.toggle_button)
        self.ui.load_pages.row_4_layout.addWidget(self.line_edit)
        self.ui.load_pages.row_4_layout.addWidget(self.icon_button_2)
        self.ui.load_pages.row_4_layout.addWidget(self.icon_button_3)
        # pallete = QPalette()
        # pallete.setColor(QPalette.Text, "")
        # self.line_edit.setPalette(pallete)

        # RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////

        # BTN 1
        self.right_btn_1 = PyPushButton(
            text="Show Menu 2",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_right = QIcon(Functions.set_svg_icon("icon_arrow_right.svg"))
        self.right_btn_1.setIcon(self.icon_right)
        self.right_btn_1.setMaximumHeight(40)
        self.right_btn_1.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_2
        ))
        self.ui.right_column.btn_1_layout.addWidget(self.right_btn_1)

        # BTN 2
        self.right_btn_2 = PyPushButton(
            text="Show Menu 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_left = QIcon(Functions.set_svg_icon("icon_arrow_left.svg"))
        self.right_btn_2.setIcon(self.icon_left)
        self.right_btn_2.setMaximumHeight(40)
        self.right_btn_2.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_1
        ))
        self.ui.right_column.btn_2_layout.addWidget(self.right_btn_2)

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)
