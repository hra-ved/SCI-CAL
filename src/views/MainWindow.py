from PyQt6.QtWidgets import QMainWindow, QPushButton, QGridLayout, QVBoxLayout, QStackedWidget, QMenuBar, QMenu, \
    QApplication
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction
from src.views.CentralWidget import CentralWidget
from src.model.Settings import Settings
from src.controllers.Functions import translate, set_language, read_from_json, get_text_from_mode, set_mode, get_mode
from src.controllers.Action import Action
import hjson
from functools import partial


# noinspection PyTypeChecker
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(translate("app-name"))
        self.setFixedSize(QSize(800, 500))
        # icon source: https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
        self.setWindowIcon(QIcon("res/app_icon_64.svg"))

        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)
        display = [0, 0]
        display[0], self.calc_widget = CentralWidget.create_calculator_widget("calculator")
        display[1], self.sci_widget = CentralWidget.create_calculator_widget("scientific")

        self.side_menu_layout = MainWindow.create_side_menu(self)
        self.main_layout.addLayout(self.side_menu_layout, 0, 0, alignment=Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(MainWindow.create_menu_bar(self, display), 0, 0, alignment=Qt.AlignmentFlag.AlignTop)

        self.central_widget = QStackedWidget()
        self.central_widget.addWidget(self.calc_widget)
        self.central_widget.addWidget(self.sci_widget)
        self.central_widget.addWidget(CentralWidget.create_matrix_widget(self))
        self.central_widget.addWidget(CentralWidget.create_bitwise_widget(self))
        self.main_layout.addWidget(self.central_widget, 0, 1, alignment=Qt.AlignmentFlag.AlignTop)

    def create_menu_bar(self, display):
        self.menu_bar = QMenuBar(self)

        self.file = self.menu_bar.addMenu(translate("file"))
        self.quit = self.file.addAction(translate("quit"))

        self.edit = self.menu_bar.addMenu(translate("edit"))
        self.cut = self.edit.addAction(translate("cut"))
        self.copy = self.edit.addAction(translate("copy"))
        self.paste = self.edit.addAction(translate("paste"))

        clipboard = QApplication.clipboard()

        self.quit.triggered.connect(lambda: exit(0))
        self.cut.triggered.connect(lambda: [clipboard.setText(get_text_from_mode(
            display[0 if get_mode() == "calc" else 1])), display[0 if get_mode() == "calc" else 1].setText("")])
        self.copy.triggered.connect(lambda: clipboard.setText(get_text_from_mode(
            display[0 if get_mode() == "calc" else 1])))
        self.paste.triggered.connect(lambda: display[0 if get_mode() == "calc" else 1].setText(clipboard.text()))
        self.settings = QMenu(translate("settings"))
        self.lang = QMenu(translate("languages"))

        self.functions = self.menu_bar.addMenu(translate("functions"))
        self.function_types = [key for key in hjson.load(open("json/functions.hjson")).keys()]
        self.function_types_d = {}
        for function_type in self.function_types:
            self.function_types_d[function_type] = QMenu(function_type)
            self.functions_d = {}
            self.data = read_from_json('json/functions.hjson', "r", 1, [function_type])
            for symbol, real in self.data.items():
                self.functions_d[real] = self.function_types_d[function_type].addAction(symbol)
            self.functions.addMenu(self.function_types_d[function_type])
            Action(action=self.functions_d, display=display[1]).connect_signals()

        self.constants_menu = self.menu_bar.addMenu(translate("constants"))
        self.constant_types = [key for key in hjson.load(open("json/constants.hjson")).keys()]
        self.constant_types_d = {}
        for constant_type in self.constant_types:
            self.constant_types_d[constant_type] = QMenu(translate(constant_type))
            self.constants = {}
            self.data = read_from_json('json/constants.hjson', "r", 1, [constant_type])
            for symbol, value in self.data.items():
                self.constants[symbol] = self.constant_types_d[constant_type].addAction(symbol[1:])
            self.constants_menu.addMenu(self.constant_types_d[constant_type])
            Action(action=self.constants, display=display[1]).connect_signals()

        self.languages = {}
        languages_l = [key for key in hjson.load(open("json/localisation.hjson")).keys()]
        for language in languages_l:
            self.languages[language] = QAction(language)
            self.languages[language].setCheckable(True)
            self.lang.addAction(self.languages[language])
            if language == Settings.read_settings("Language", "language"):
                self.languages[language].setChecked(True)
            self.languages[language].triggered.connect(partial(set_language, language, self.languages))

        self.menu_bar.addMenu(self.settings)
        self.settings.addMenu(self.lang)

        return self.menu_bar

    def create_side_menu(self):
        side_menu_layout = QVBoxLayout()
        standard = QPushButton(translate("standard"))
        scientific = QPushButton(translate("scientific"))
        matrix = QPushButton(translate("matrix"))
        bitwise = QPushButton(translate("bitwise"))

        standard.clicked.connect(lambda: [self.central_widget.setCurrentIndex(0), set_mode("calc"), self.setFixedSize(QSize(800, 500))])
        scientific.clicked.connect(lambda: [self.central_widget.setCurrentIndex(1), set_mode("sci"), self.setFixedSize(QSize(800, 500))])
        matrix.clicked.connect(lambda: [self.central_widget.setCurrentIndex(2), set_mode("matrix"), self.setFixedSize(QSize(1200, 500))])
        bitwise.clicked.connect(lambda: [self.central_widget.setCurrentIndex(3), set_mode("bitwise"), self.setFixedSize(QSize(800, 500))])
        side_menu_layout.addWidget(standard)
        side_menu_layout.addWidget(scientific)
        side_menu_layout.addWidget(matrix)
        side_menu_layout.addWidget(bitwise)

        return side_menu_layout
from PyQt6.QtWidgets import QMainWindow, QPushButton, QGridLayout, QVBoxLayout, QStackedWidget, QMenuBar, QMenu, \
    QApplication
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction
from src.views.CentralWidget import CentralWidget
from src.model.Settings import Settings
from src.controllers.Functions import translate, set_language, read_from_json, get_text_from_mode, set_mode, get_mode
from src.controllers.Action import Action
import hjson
from functools import partial
from sys import platform as sys_platform


# noinspection PyTypeChecker
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(translate("app-name"))
        self.setFixedSize(QSize(800, 500))
        # icon source: https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
        self.setWindowIcon(QIcon("res/app_icon_64.svg"))

        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)
        display = [0, 0]
        display[0], self.calc_widget = CentralWidget.create_calculator_widget("calculator")
        display[1], self.sci_widget = CentralWidget.create_calculator_widget("scientific")

        self.side_menu_layout = MainWindow.create_side_menu(self)
        self.main_layout.addLayout(self.side_menu_layout, 0, 0, alignment=Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(MainWindow.create_menu_bar(self, display), 0, 0, alignment=Qt.AlignmentFlag.AlignTop)

        self.central_widget = QStackedWidget()
        self.central_widget.addWidget(self.calc_widget)
        self.central_widget.addWidget(self.sci_widget)
        self.central_widget.addWidget(CentralWidget.create_matrix_widget(self))
        self.central_widget.addWidget(CentralWidget.create_bitwise_widget(self))
        self.main_layout.addWidget(self.central_widget, 0, 1, alignment=Qt.AlignmentFlag.AlignTop)

    def create_menu_bar(self, display):
        self.menu_bar = QMenuBar(self)

        self.file = self.menu_bar.addMenu(translate("file"))
        self.quit = self.file.addAction(translate("quit"))

        self.edit = self.menu_bar.addMenu(translate("edit"))
        self.cut = self.edit.addAction(translate("cut"))
        self.copy = self.edit.addAction(translate("copy"))
        self.paste = self.edit.addAction(translate("paste"))

        clipboard = QApplication.clipboard()

        self.quit.triggered.connect(lambda: exit(0))
        self.cut.triggered.connect(lambda: [clipboard.setText(get_text_from_mode(
            display[0 if get_mode() == "calc" else 1])), display[0 if get_mode() == "calc" else 1].setText("")])
        self.copy.triggered.connect(lambda: clipboard.setText(get_text_from_mode(
            display[0 if get_mode() == "calc" else 1])))
        self.paste.triggered.connect(lambda: display[0 if get_mode() == "calc" else 1].setText(clipboard.text()))
        self.settings = QMenu(translate("settings"))
        self.lang = QMenu(translate("languages"))

        self.functions = self.menu_bar.addMenu(translate("functions"))
        self.function_types = [key for key in hjson.load(open("json/functions.hjson", encoding="utf-8")).keys()]
        self.function_types_d = {}
        for function_type in self.function_types:
            self.function_types_d[function_type] = QMenu(function_type)
            self.functions_d = {}
            self.data = read_from_json('json/functions.hjson', "r", 1, [function_type])
            for symbol, real in self.data.items():
                self.functions_d[real] = self.function_types_d[function_type].addAction(symbol)
            self.functions.addMenu(self.function_types_d[function_type])
            Action(action=self.functions_d, display=display[1]).connect_signals()

        self.constants_menu = self.menu_bar.addMenu(translate("constants"))
        self.constant_types = [key for key in hjson.load(open("json/constants.hjson", encoding="utf-8")).keys()]
        self.constant_types_d = {}
        for constant_type in self.constant_types:
            self.constant_types_d[constant_type] = QMenu(translate(constant_type))
            self.constants = {}
            self.data = read_from_json('json/constants.hjson', "r", 1, [constant_type])
            for symbol, value in self.data.items():
                self.constants[symbol] = self.constant_types_d[constant_type].addAction(symbol[1:])
            self.constants_menu.addMenu(self.constant_types_d[constant_type])
            Action(action=self.constants, display=display[1]).connect_signals()

        self.languages = {}
        languages_l = [key for key in hjson.load(open("json/localisation.hjson", encoding="utf-8")).keys()]
        for language in languages_l:
            self.languages[language] = QAction(language)
            self.languages[language].setCheckable(True)
            self.lang.addAction(self.languages[language])
            if language == Settings.read_settings("Language", "language"):
                self.languages[language].setChecked(True)
            self.languages[language].triggered.connect(partial(set_language, language, self.languages))

        self.menu_bar.addMenu(self.settings)
        self.settings.addMenu(self.lang)

        return self.menu_bar

    def create_side_menu(self):
        side_menu_layout = QVBoxLayout()
        standard = QPushButton(translate("standard"))
        scientific = QPushButton(translate("scientific"))
        matrix = QPushButton(translate("matrix"))
        bitwise = QPushButton(translate("bitwise"))

        standard.clicked.connect(lambda: [self.central_widget.setCurrentIndex(0), set_mode("calc"), self.setFixedSize(QSize(800, 500))])
        scientific.clicked.connect(lambda: [self.central_widget.setCurrentIndex(1), set_mode("sci"), self.setFixedSize(QSize(800, 500))])
        matrix.clicked.connect(lambda: [self.central_widget.setCurrentIndex(2), set_mode("matrix"), self.setFixedSize(QSize(1200, 500))])
        bitwise.clicked.connect(lambda: [self.central_widget.setCurrentIndex(3), set_mode("bitwise"), self.setFixedSize(QSize(800, 500))])
        if sys_platform != "linux" and sys_platform != "linux2":
            side_menu_layout.addWidget(QPushButton()) # placeholder
        side_menu_layout.addWidget(standard)
        side_menu_layout.addWidget(scientific)
        side_menu_layout.addWidget(matrix)
        side_menu_layout.addWidget(bitwise)

        return side_menu_layout
