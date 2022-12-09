from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QLineEdit, QTableWidget, QTableWidgetItem, QGroupBox
from PyQt6.QtCore import Qt
from src.controllers.Functions import read_from_json
from src.controllers.CalculatorController import CalculatorController
from src.controllers.MatrixController import MatrixController
from src.controllers.BitwiseController import BitwiseController


class CentralWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(CentralWidget, self).__init__(*args, **kwargs)
        self.buttons = {"=": QPushButton("=")}
        self.add_col_a = QPushButton()

    @staticmethod
    def create_calculator_widget(mode):
        calculator_layout = QGridLayout()
        display = QLineEdit()
        display.setFixedHeight(70)
        display.setAlignment(Qt.AlignmentFlag.AlignRight)
        display.setReadOnly(True)
        calculator_layout.addWidget(display, 0, 0, 1, 5)
        calculator_widget = QGroupBox()
        data = read_from_json('json/layout.hjson', "r", 1, [mode])
        buttons = {}
        for button_text, button_coordinate in data.items():
            buttons[button_text] = QPushButton(button_text)
            buttons[button_text].setFixedSize(70, 70)
            calculator_layout.addWidget(buttons[button_text], button_coordinate[0], button_coordinate[1])
        calculator_widget.setLayout(calculator_layout)
        CalculatorController(buttons=buttons, display=display).connect_signals()

        return display, calculator_widget

    def create_matrix_widget(self):
        self.matrix_widget = QGroupBox()
        self.matrix_layout = QGridLayout()

        # matrix A
        self.matrix_a = QTableWidget()
        self.matrix_a.setObjectName("matrix_a")
        self.matrix_a.setMaximumSize(350, 350)
        self.matrix_a.setColumnCount(1)
        self.matrix_a.setRowCount(1)
        self.matrix_a.setColumnWidth(0, 50)
        self.matrix_a.setItem(0, 0, QTableWidgetItem("0"))
        self.matrix_layout.addWidget(self.matrix_a, 2, 0, 4, 3)

        # matrix B
        self.matrix_b = QTableWidget()
        self.matrix_b.setObjectName("matrix_b")
        self.matrix_b.setMaximumSize(350, 350)
        self.matrix_b.setColumnCount(1)
        self.matrix_b.setRowCount(1)
        self.matrix_b.setColumnWidth(0, 50)
        self.matrix_b.setItem(0, 0, QTableWidgetItem(" "))
        self.matrix_layout.addWidget(self.matrix_b, 2, 4, 4, 3)

        # matrix C
        self.matrix_c = QTableWidget()
        self.matrix_c.setObjectName("matrix_c")
        self.matrix_c.setMaximumSize(350, 350)
        self.matrix_c.setColumnCount(1)
        self.matrix_c.setRowCount(1)
        self.matrix_c.setColumnWidth(0, 50)
        self.matrix_c.setItem(0, 0, QTableWidgetItem("0"))
        self.matrix_layout.addWidget(self.matrix_c, 2, 8, 4, 3)

        # operations
        self.button_add = QPushButton("+")
        self.button_add.setObjectName("+")
        self.button_sub = QPushButton('-')
        self.button_sub.setObjectName("-")
        self.buttons_mul_mat = QPushButton('x')
        self.buttons_mul_mat.setObjectName('X')
        self.button_sca_mat = QPushButton('x')
        self.button_sca_mat.setObjectName("x")
        self.matrix_layout.addWidget(self.button_add, 2, 3)
        self.matrix_layout.addWidget(self.button_sub, 3, 3)
        self.matrix_layout.addWidget(self.button_sca_mat, 4, 3)
        self.matrix_layout.addWidget(self.buttons_mul_mat, 5, 3)

        # manipulation A
        self.add_col_a = QPushButton("Dodaj stupac")
        self.add_col_a.setObjectName("add_col_a")
        self.add_row_a = QPushButton("Dodaj redak")
        self.add_row_a.setObjectName("add_row_a")
        self.add_col_row_a = QPushButton("Dodaj st. i red.")
        self.add_col_row_a.setObjectName("add_col_row_a")
        self.rem_col_a = QPushButton("Izbriši stupac")
        self.rem_col_a.setObjectName("rem_col_a")
        self.rem_row_a = QPushButton("Izbriši redak")
        self.rem_row_a.setObjectName("rem_row_a")
        self.rem_col_row_a = QPushButton("Izbriši st. i red.")
        self.rem_col_row_a.setObjectName("rem_col_row_a")
        self.matrix_layout.addWidget(self.add_col_a, 0, 0)
        self.matrix_layout.addWidget(self.add_row_a, 0, 1)
        self.matrix_layout.addWidget(self.add_col_row_a, 0, 2)
        self.matrix_layout.addWidget(self.rem_col_a, 1, 0)
        self.matrix_layout.addWidget(self.rem_row_a, 1, 1)
        self.matrix_layout.addWidget(self.rem_col_row_a, 1, 2)

        # manipulation B
        self.add_col_b = QPushButton("Dodaj stupac")
        self.add_col_b.setObjectName("add_col_b")
        self.add_row_b = QPushButton("Dodaj redak")
        self.add_row_b.setObjectName("add_row_b")
        self.add_col_row_b = QPushButton("Dodaj st. i red.")
        self.add_col_row_b.setObjectName("add_col_row_b")
        self.rem_col_b = QPushButton("Izbriši stupac")
        self.rem_col_b.setObjectName("rem_col_b")
        self.rem_row_b = QPushButton("Izbriši redak")
        self.rem_row_b.setObjectName("rem_row_b")
        self.rem_col_row_b = QPushButton("Izbriši st. i red.")
        self.rem_col_row_b.setObjectName("rem_col_row_b")
        self.matrix_layout.addWidget(self.add_col_b, 0, 4)
        self.matrix_layout.addWidget(self.add_row_b, 0, 5)
        self.matrix_layout.addWidget(self.add_col_row_b, 0, 6)
        self.matrix_layout.addWidget(self.rem_col_b, 1, 4)
        self.matrix_layout.addWidget(self.rem_row_b, 1, 5)
        self.matrix_layout.addWidget(self.rem_col_row_b, 1, 6)

        # operations A
        self.determinant_a = QPushButton("Determinanta")
        self.determinant_a.setObjectName("det_a")
        self.inversion_a = QPushButton("Inversion")
        self.inversion_a.setObjectName("inv_a")
        self.import_a = QPushButton("Uvezi")
        self.import_a.setObjectName("imp_a")
        self.transpose_a = QPushButton("Transponiraj")
        self.transpose_a.setObjectName("tra_a")
        self.pse_ran_a = QPushButton("Pseudo-Random")
        self.pse_ran_a.setObjectName("pr_a")
        self.export_a = QPushButton("Izvezi")
        self.export_a.setObjectName("exp_a")
        self.matrix_layout.addWidget(self.determinant_a, 6, 0)
        self.matrix_layout.addWidget(self.inversion_a, 6, 1)
        self.matrix_layout.addWidget(self.import_a, 6, 2)
        self.matrix_layout.addWidget(self.transpose_a, 7, 0)
        self.matrix_layout.addWidget(self.pse_ran_a, 7, 1)
        self.matrix_layout.addWidget(self.export_a, 7, 2)

        # operations B
        self.determinant_b = QPushButton("Determinanta")
        self.determinant_b.setObjectName("det_b")
        self.inversion_b = QPushButton("Inversion")
        self.inversion_b.setObjectName("inv_b")
        self.import_b = QPushButton("Uvezi")
        self.import_b.setObjectName("imp_b")
        self.transpose_b = QPushButton("Transponiraj")
        self.transpose_b.setObjectName("tra_b")
        self.pse_ran_b = QPushButton("Pseudo-Random")
        self.pse_ran_b.setObjectName("pr_b")
        self.export_b = QPushButton("Izvezi")
        self.export_b.setObjectName("exp_b")
        self.matrix_layout.addWidget(self.determinant_b, 6, 4)
        self.matrix_layout.addWidget(self.inversion_b, 6, 5)
        self.matrix_layout.addWidget(self.import_b, 6, 6)
        self.matrix_layout.addWidget(self.transpose_b, 7, 4)
        self.matrix_layout.addWidget(self.pse_ran_b, 7, 5)
        self.matrix_layout.addWidget(self.export_b, 7, 6)

        MatrixController(layout=self.matrix_layout).connect_signals()

        self.matrix_widget.setLayout(self.matrix_layout)
        return self.matrix_widget

    def create_bitwise_widget(self):
        bitwise_layout = QGridLayout()
        display = QLineEdit()
        display.setFixedHeight(70)
        display.setAlignment(Qt.AlignmentFlag.AlignRight)
        display.setReadOnly(False)
        bitwise_layout.addWidget(display, 0, 0, 1, 5)
        calculator_widget = QGroupBox()
        data = read_from_json('json/layout.hjson', "r", 1, ["bitwise"])
        buttons = {}
        for button_text, button_coordinate in data.items():
            buttons[button_text] = QPushButton(button_text)
            buttons[button_text].setFixedSize(70, 70)
            bitwise_layout.addWidget(buttons[button_text], button_coordinate[0], button_coordinate[1])
        calculator_widget.setLayout(bitwise_layout)
        BitwiseController(buttons=buttons, display=display).connect_signals()

        return calculator_widget


from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QLineEdit, QTableWidget, QTableWidgetItem, QGroupBox
from PyQt6.QtCore import Qt
from src.controllers.Functions import read_from_json, translate
from src.controllers.CalculatorController import CalculatorController
from src.controllers.MatrixController import MatrixController
from src.controllers.BitwiseController import BitwiseController


# noinspection PyTypeChecker
class CentralWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(CentralWidget, self).__init__(*args, **kwargs)

    @staticmethod
    def create_calculator_widget(mode):
        calculator_layout = QGridLayout()
        display = QLineEdit()
        display.setFixedHeight(70)
        display.setAlignment(Qt.AlignmentFlag.AlignRight)
        display.setReadOnly(True)
        calculator_layout.addWidget(display, 0, 0, 1, 5)
        calculator_widget = QGroupBox()
        data = read_from_json('json/layout.hjson', "r", 1, [mode])
        buttons = {}
        for button_text, button_coordinate in data.items():
            buttons[button_text] = QPushButton(button_text)
            buttons[button_text].setFixedSize(70, 70)
            calculator_layout.addWidget(buttons[button_text], button_coordinate[0], button_coordinate[1])
        calculator_widget.setLayout(calculator_layout)
        CalculatorController(buttons=buttons, display=display).connect_signals()

        return display, calculator_widget

    def create_matrix_widget(self):
        self.matrix_widget = QGroupBox()
        self.matrix_layout = QGridLayout()

        # matrix A
        self.matrix_a = QTableWidget()
        self.matrix_a.setObjectName("matrix_a")
        self.matrix_a.setMaximumSize(350, 350)
        self.matrix_a.setColumnCount(1)
        self.matrix_a.setRowCount(1)
        self.matrix_a.setColumnWidth(0, 50)
        self.matrix_a.setItem(0, 0, QTableWidgetItem("0"))
        self.matrix_layout.addWidget(self.matrix_a, 2, 0, 4, 3)

        # matrix B
        self.matrix_b = QTableWidget()
        self.matrix_b.setObjectName("matrix_b")
        self.matrix_b.setMaximumSize(350, 350)
        self.matrix_b.setColumnCount(1)
        self.matrix_b.setRowCount(1)
        self.matrix_b.setColumnWidth(0, 50)
        self.matrix_b.setItem(0, 0, QTableWidgetItem(" "))
        self.matrix_layout.addWidget(self.matrix_b, 2, 4, 4, 3)

        # matrix C
        self.matrix_c = QTableWidget()
        self.matrix_c.setObjectName("matrix_c")
        self.matrix_c.setMaximumSize(350, 350)
        self.matrix_c.setColumnCount(1)
        self.matrix_c.setRowCount(1)
        self.matrix_c.setColumnWidth(0, 50)
        self.matrix_c.setItem(0, 0, QTableWidgetItem("0"))
        self.matrix_layout.addWidget(self.matrix_c, 2, 8, 4, 3)

        # operations
        self.button_add = QPushButton("+")
        self.button_add.setObjectName("+")
        self.button_sub = QPushButton('-')
        self.button_sub.setObjectName("-")
        self.buttons_mul_mat = QPushButton('x')
        self.buttons_mul_mat.setObjectName('X')
        self.button_sca_mat = QPushButton('x')
        self.button_sca_mat.setObjectName("x")
        self.matrix_layout.addWidget(self.button_add, 2, 3)
        self.matrix_layout.addWidget(self.button_sub, 3, 3)
        self.matrix_layout.addWidget(self.button_sca_mat, 4, 3)
        self.matrix_layout.addWidget(self.buttons_mul_mat, 5, 3)

        # manipulation A
        self.add_col_a = QPushButton(translate("add-col"))
        self.add_col_a.setObjectName("add_col_a")
        self.add_row_a = QPushButton(translate("add-row"))
        self.add_row_a.setObjectName("add_row_a")
        self.add_col_row_a = QPushButton(translate("add-row-col"))
        self.add_col_row_a.setObjectName("add_col_row_a")
        self.rem_col_a = QPushButton(translate("del-col"))
        self.rem_col_a.setObjectName("rem_col_a")
        self.rem_row_a = QPushButton(translate("del-row"))
        self.rem_row_a.setObjectName("rem_row_a")
        self.rem_col_row_a = QPushButton(translate("del-row-col"))
        self.rem_col_row_a.setObjectName("rem_col_row_a")
        self.matrix_layout.addWidget(self.add_col_a, 0, 0)
        self.matrix_layout.addWidget(self.add_row_a, 0, 1)
        self.matrix_layout.addWidget(self.add_col_row_a, 0, 2)
        self.matrix_layout.addWidget(self.rem_col_a, 1, 0)
        self.matrix_layout.addWidget(self.rem_row_a, 1, 1)
        self.matrix_layout.addWidget(self.rem_col_row_a, 1, 2)

        # manipulation B
        self.add_col_b = QPushButton(translate("add-col"))
        self.add_col_b.setObjectName("add_col_b")
        self.add_row_b = QPushButton(translate("add-row"))
        self.add_row_b.setObjectName("add_row_b")
        self.add_col_row_b = QPushButton(translate("add-row-col"))
        self.add_col_row_b.setObjectName("add_col_row_b")
        self.rem_col_b = QPushButton(translate("del-col"))
        self.rem_col_b.setObjectName("rem_col_b")
        self.rem_row_b = QPushButton(translate("del-row"))
        self.rem_row_b.setObjectName("rem_row_b")
        self.rem_col_row_b = QPushButton(translate("del-row-col"))
        self.rem_col_row_b.setObjectName("rem_col_row_b")
        self.matrix_layout.addWidget(self.add_col_b, 0, 4)
        self.matrix_layout.addWidget(self.add_row_b, 0, 5)
        self.matrix_layout.addWidget(self.add_col_row_b, 0, 6)
        self.matrix_layout.addWidget(self.rem_col_b, 1, 4)
        self.matrix_layout.addWidget(self.rem_row_b, 1, 5)
        self.matrix_layout.addWidget(self.rem_col_row_b, 1, 6)

        # operations A
        self.determinant_a = QPushButton(translate("det"))
        self.determinant_a.setObjectName("det_a")
        self.inversion_a = QPushButton(translate("inv"))
        self.inversion_a.setObjectName("inv_a")
        self.import_a = QPushButton(translate("import"))
        self.import_a.setObjectName("imp_a")
        self.transpose_a = QPushButton(translate("trans"))
        self.transpose_a.setObjectName("tra_a")
        self.pse_ran_a = QPushButton(translate("p-r"))
        self.pse_ran_a.setObjectName("pr_a")
        self.export_a = QPushButton(translate("export"))
        self.export_a.setObjectName("exp_a")
        self.matrix_layout.addWidget(self.determinant_a, 6, 0)
        self.matrix_layout.addWidget(self.inversion_a, 6, 1)
        self.matrix_layout.addWidget(self.import_a, 6, 2)
        self.matrix_layout.addWidget(self.transpose_a, 7, 0)
        self.matrix_layout.addWidget(self.pse_ran_a, 7, 1)
        self.matrix_layout.addWidget(self.export_a, 7, 2)

        # operations B
        self.determinant_b = QPushButton(translate("det"))
        self.determinant_b.setObjectName("det_b")
        self.inversion_b = QPushButton(translate("inv"))
        self.inversion_b.setObjectName("inv_b")
        self.import_b = QPushButton(translate("import"))
        self.import_b.setObjectName("imp_b")
        self.transpose_b = QPushButton(translate("trans"))
        self.transpose_b.setObjectName("tra_b")
        self.pse_ran_b = QPushButton(translate("p-r"))
        self.pse_ran_b.setObjectName("pr_b")
        self.export_b = QPushButton(translate("export"))
        self.export_b.setObjectName("exp_b")
        self.matrix_layout.addWidget(self.determinant_b, 6, 4)
        self.matrix_layout.addWidget(self.inversion_b, 6, 5)
        self.matrix_layout.addWidget(self.import_b, 6, 6)
        self.matrix_layout.addWidget(self.transpose_b, 7, 4)
        self.matrix_layout.addWidget(self.pse_ran_b, 7, 5)
        self.matrix_layout.addWidget(self.export_b, 7, 6)

        MatrixController(layout=self.matrix_layout).connect_signals()

        self.matrix_widget.setLayout(self.matrix_layout)
        return self.matrix_widget

    def create_bitwise_widget(self):
        bitwise_layout = QGridLayout()
        display = QLineEdit()
        display.setFixedHeight(70)
        display.setAlignment(Qt.AlignmentFlag.AlignRight)
        display.setReadOnly(False)
        bitwise_layout.addWidget(display, 0, 0, 1, 5)
        calculator_widget = QGroupBox()
        data = read_from_json('json/layout.hjson', "r", 1, ["bitwise"])
        buttons = {}
        for button_text, button_coordinate in data.items():
            buttons[button_text] = QPushButton(button_text)
            buttons[button_text].setFixedSize(70, 70)
            bitwise_layout.addWidget(buttons[button_text], button_coordinate[0], button_coordinate[1])
        calculator_widget.setLayout(bitwise_layout)
        BitwiseController(buttons=buttons, display=display).connect_signals()

        return calculator_widget

