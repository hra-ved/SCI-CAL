from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox, QFileDialog
from src.controllers.MathOperations import *
from src.controllers.Functions import translate
import numpy as np


class MatrixController:
    def __init__(self, layout, *args, **kwargs):
        super(MatrixController, self).__init__(*args, **kwargs)
        self.layout = layout
        indx = self.layout.count()
        self.widgets = {}
        while indx > 0:
            indx -= 1
            widget = self.layout.itemAt(indx).widget()
            name = self.layout.itemAt(indx).widget().objectName()
            self.widgets[name] = widget

    def connect_signals(self):
        self.signals = {
            "add_row_a": "add_row(self, 'a')",
            "add_col_a": "add_col(self, 'a')",
            "add_col_row_a": "add_col_row(self, 'a')",
            "rem_row_a": "rem_row(self, 'a')",
            "rem_col_a": "rem_col(self, 'a')",
            "rem_col_row_a": "rem_col_row(self, 'a')",
            "det_a": "determinant(self, 'a')",
            "inv_a": "invert(self, 'a')",
            "imp_a": "import_mat(self, 'a')",
            "tra_a": "transpose(self, 'a')",
            "pr_a": "pseudo_random(self, 'a')",
            "exp_a": "export_mat(self, 'a')",

            "add_row_b": "add_row(self, 'b')",
            "add_col_b": "add_col(self, 'b')",
            "add_col_row_b": "add_col_row(self, 'b')",
            "rem_row_b": "rem_row(self, 'b')",
            "rem_col_b": "rem_col(self, 'b')",
            "rem_col_row_b": "rem_col_row(self, 'b')",
            "det_b": "determinant(self, 'b')",
            "inv_b": "invert(self, 'b')",
            "imp_b": "import_mat(self, 'b')",
            "tra_b": "transpose(self, 'b')",
            "pr_b": "pseudo_random(self, 'b')",
            "exp_b": "export_mat(self, 'b')",
            "+": "matrix_addition(self)",
            "-": "matrix_subtraction(self)",
            "X": "matrix_multiplication(self)",
            "x": "matrix_multiplication_sca(self)"
        }

        for key, widget in self.widgets.items():
            if key not in {"matrix_a", "matrix_b", "matrix_c"}:
                widget.clicked.connect(
                    lambda param, key=key: [eval("MatrixController." + self.signals[key])])  # QT param

    def find_widget(self, widget_id):
        for indx in range(self.layout.count()):
            if self.layout.itemAt(indx).widget().objectName() == widget_id:
                return self.layout.itemAt(indx).widget()

    def add_col(self, matrix_id):
        matrix_id = "matrix_" + matrix_id
        widget = MatrixController.find_widget(self, matrix_id)
        num_of_cols = widget.columnCount()
        widget.setColumnCount(num_of_cols + 1)
        widget.setColumnWidth(num_of_cols, 50)

    def add_row(self, matrix_id):
        matrix_id = "matrix_" + matrix_id
        widget = MatrixController.find_widget(self, matrix_id)
        num_of_rows = widget.rowCount()
        widget.setRowCount(num_of_rows + 1)

    def rem_col(self, matrix_id):
        matrix_id = "matrix_" + matrix_id
        widget = MatrixController.find_widget(self, matrix_id)
        num_of_cols = widget.columnCount()
        widget.setColumnCount(num_of_cols - 1)

    def rem_row(self, matrix_id):
        matrix_id = "matrix_" + matrix_id
        widget = MatrixController.find_widget(self, matrix_id)
        num_of_rows = widget.rowCount()
        widget.setRowCount(num_of_rows - 1)

    def add_col_row(self, matrix_id):
        MatrixController.add_col(self, matrix_id)
        MatrixController.add_row(self, matrix_id)

    def rem_col_row(self, matrix_id):
        MatrixController.rem_col(self, matrix_id)
        MatrixController.rem_row(self, matrix_id)

    def determinant(self, matrix_id):
        matrix = MatrixController.read_from_matrix(self, matrix_id)
        if len(matrix) == len(matrix[0]):
            result = round(matrix_determinant(matrix), 2)
            self.error_msg(f"D={result}", "Determinant", "")
        else:
            self.error_msg(translate("determinant-text"), translate("determinant-title"), translate("determinant-extra"))

    def invert(self, matrix_id):
        matrix = MatrixController.read_from_matrix(self, matrix_id)
        try:
            matrix = matrix_inversion(matrix)
            MatrixController.write_to_matrix(self, matrix_id, matrix)
        except np.linalg.LinAlgError:
            self.error_msg(translate("matrix-text"), translate("matrix-title"), translate("matrix-extra"))

    def transpose(self, matrix_id):
        matrix = MatrixController.read_from_matrix(self, matrix_id)
        matrix = matrix_transpose(matrix)
        MatrixController.set_dimensions(self, matrix_id, len(matrix[0]), len(matrix))
        MatrixController.write_to_matrix(self, matrix_id, matrix)

    def pseudo_random(self, matrix_id):
        new_matrix_id = "matrix_" + matrix_id
        widget = MatrixController.find_widget(self, new_matrix_id)
        matrix = np.random.random([widget.rowCount(), widget.columnCount()]) * 10
        matrix.astype(int)
        MatrixController.write_to_matrix(self, matrix_id, matrix)

    def matrix_addition(self):
        matrix_a = MatrixController.read_from_matrix(self, "a")
        matrix_b = MatrixController.read_from_matrix(self, "b")
        if len(matrix_a) == len(matrix_b) and len(matrix_a[0]) == len(matrix_b[0]):
            matrix_c = add_matrices(matrix_a, matrix_b)
            MatrixController.set_dimensions(self, "c", len(matrix_a), len(matrix_a))
            MatrixController.write_to_matrix(self, "c", matrix_c)
        else:
            self.error_msg(translate("addition-text"), translate("addition-title"), translate("addition-extra"))

    def matrix_subtraction(self):
        matrix_a = MatrixController.read_from_matrix(self, "a")
        matrix_b = MatrixController.read_from_matrix(self, "b")
        if len(matrix_a) == len(matrix_b) and len(matrix_a[0]) == len(matrix_b[0]):
            matrix_c = subtract_matrices(matrix_a, matrix_b)
            MatrixController.set_dimensions(self, "c", len(matrix_a), len(matrix_a))
            MatrixController.write_to_matrix(self, "c", matrix_c)
        else:
            self.error_msg(translate("subs-text"), translate("subs-title"), translate("subs-extra"))

    def matrix_multiplication(self):
        matrix_a = MatrixController.read_from_matrix(self, "a")
        matrix_b = MatrixController.read_from_matrix(self, "b")
        if len(matrix_a) == len(matrix_b[0]) and len(matrix_a[0]) == len(matrix_b):
            matrix_c = multiply_matrices(matrix_a, matrix_b)
            MatrixController.set_dimensions(self, "c", len(matrix_a), len(matrix_a))
            MatrixController.write_to_matrix(self, "c", matrix_c)
        else:
            self.error_msg(translate("mul-text"), translate("mul-title"), translate("mul-extra"))

    def matrix_multiplication_sca(self):
        matrix_a = MatrixController.read_from_matrix(self, "a")
        matrix_b = MatrixController.read_from_matrix(self, "b")
        if len(matrix_b) == 1 and len(matrix_b[0]) == 1:
            matrix_c = multiple_matrice_scalar(matrix_a, matrix_b[0][0])
            MatrixController.set_dimensions(self, "c", len(matrix_a[0]), len(matrix_a))
            MatrixController.write_to_matrix(self, "c", matrix_c)
        else:
            self.error_msg(translate("sca-text"), translate("sca-title"), translate("sca-extra"))

    def import_mat(self, matrix_id):
        file = QFileDialog.getOpenFileName(caption=translate("open-file"), directory="/home", initialFilter="Files (*.cal)")
        content = open(file[0]).readlines()
        content = open(file[0], encoding="utf-8").readlines()
        matrix = []
        for line in content:
            row = line.split()
            temp = []
            for col in range(len(row)):
                temp.append(row[col])
            matrix.append(temp)
        self.write_to_matrix(matrix_id, matrix)

    def export_mat(self, matrix_id):
        file = QFileDialog.getOpenFileName(caption=translate("open-file"), directory="/home", initialFilter="Files (*.cal)")
        file = open(file[0], "w")
        file = open(file[0], "w", encoding="utf-8")
        matrix = self.read_from_matrix(matrix_id).astype(str)
        for line in matrix:
            file.write(" ".join(line)+"\n")

    def read_from_matrix(self, matrix_id):
        matrix_id = "matrix_" + matrix_id
        widget = MatrixController.find_widget(self, matrix_id)
        matrix = np.zeros(shape=(widget.rowCount(), widget.columnCount()))
        for i in range(widget.rowCount()):
            for j in range(widget.columnCount()):
                matrix[i][j] = float(widget.item(i, j).text())
        return matrix

    def write_to_matrix(self, matrix_id, matrix):
        matrix_id = "matrix_" + matrix_id
        widget = MatrixController.find_widget(self, matrix_id)
        widget.setRowCount(len(matrix))
        widget.setColumnCount(len(matrix[0]))
        for i in range(widget.rowCount()):
            for j in range(widget.columnCount()):
                widget.setColumnWidth(j, 50)
                widget.setItem(i, j, QTableWidgetItem(str(matrix[i][j])))

    def set_dimensions(self, matrix_id, col, row):
        matrix_id = "matrix_" + matrix_id
        widget = MatrixController.find_widget(self, matrix_id)
        widget.setColumnCount(col)
        widget.setRowCount(row)

    def error_msg(self, error_msg, error_title, error_details):
        self.error_widget = QMessageBox()
        self.error_widget.setText(error_msg)
        self.error_widget.setWindowTitle(error_title)
        self.error_widget.setDetailedText(error_details)
        self.error_widget.exec()
