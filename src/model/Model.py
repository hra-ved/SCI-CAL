from PyQt6.QtWidgets import QMessageBox
from src.controllers.Functions import read_from_json, translate
import numpy as np


class Model:
    def __init__(self, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self.data = None

    def evaluate_expression(self, expression):
        error_dialog = QMessageBox()
        # error_dialog.setIcon(QMessageBox.critical)
        result = ''
        try:
            expression = Model.normalize(self, expression)
            result = str(eval(expression, {"np": np}, {"i": "i"}))
        except ZeroDivisionError:
            error_dialog.setText(translate("0-text"))
            error_dialog.setWindowTitle(translate("0-title"))
            error_dialog.setInformativeText(translate("0-extra"))
            error_dialog.exec()
        except SyntaxError:
            error_dialog.setText(translate("syntax-text"))
            error_dialog.setWindowTitle(translate("syntax-title"))
            error_dialog.setInformativeText(translate("syntax-extra"))
            error_dialog.exec()

        return result

    def normalize(self, expression):
        # constants
        constant_types = ["Universal", "Electromagnetic", "Atomic and Nuclear", "Phy-Chem", "Adopted Values"]
        for constant_type in constant_types:
            self.data = read_from_json('json/constants.hjson', "r", 1, [constant_type])
            for symbol, value in self.data.items():
                indx = value.find("//")
                expression = expression.replace(symbol, value[:indx])
                print(expression)

        # functions
        self.data = list(read_from_json('json/functions.hjson', "r", 1, ["trigonometry"]).values())
        for value in self.data:
            if value in expression:
                expression = Model.trig(self, expression, value)
                print(expression)

        expression = Model.log(self, expression)
        expression = Model.factorial(self, expression)
        expression = Model.sqrt(self, expression)

        #bitwise
        expression = Model.bitwise(self, expression)
        return expression

    def trig(self, expression, value):
        if "arc" in value:
            expression = expression.replace("arc", "np.arc")
        else:
            indx = expression.find(value)
            if indx > 0:
                if expression[indx-1] != 'c':
                    expression = expression[:indx] + "np." + expression[indx:]
            else:
                expression = "np." + expression
        return expression

    def log(self, expression):
        if 'log' in expression:
            indx = expression.find("log")
            indx_2 = expression.find("(", indx)
            base = int(expression[indx + 3:indx_2])

            indx_3 = expression.find(")", indx_2)
            argument = int(eval(expression[indx_2 + 1:indx_3]))
            result = np.log(argument) / np.log(base)
            old = expression[indx:indx_3 + 1]
            expression = expression.replace(old, str(result))
            return Model.log(self, expression)
        else:
            return expression

    def factorial(self, expression):
        if '!' in expression:
            indx = expression.find('!')
            indx2 = 0
            for indx_2 in range(indx - 1, 0, -1):
                if expression[indx_2] not in "0123456789.":
                    indx2 = indx_2
                    break
            indx2 -= 1 if indx2 == 0 else 0
            argument = expression[indx2 + 1:indx]
            result = str(np.math.factorial(int(argument)))
            expression = expression.replace(expression[indx2 + 1:indx + 1], result)
            return Model.factorial(self, expression)
        else:
            return expression

    def sqrt(self, expression):
        if "sqrt" in expression:
            indx = expression.find("sqrt(")
            indx2 = expression.find(")", indx)
            argument = expression[indx + 5:indx2]
            replacement = str(np.sqrt(int(argument))) if int(argument) >= 0 else str(int(argument) * -1) + "i"
            expression = expression.replace(expression[indx:indx2 + 1], replacement)
            return Model.sqrt(self, expression)
        else:
            return expression

    def bitwise(self, expression):
        expression = expression.replace("AND", "&")
        expression = expression.replace("XOR", "^" )
        expression = expression.replace("OR", "|")
        return expression

