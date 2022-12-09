from functools import partial
from src.model.Model import Model


class CalculatorController:
    def __init__(self, buttons, display,  *args, **kwargs):
        super(CalculatorController, self).__init__(*args, **kwargs)
        self.buttons = buttons
        self.display = display

    def connect_signals(self):
        for button_text, button_instance in self.buttons.items():
            if button_text not in {"=", "C", "DEL"}:
                button_instance.clicked.connect(partial(self.signal_content, button_text))
        self.buttons['='].clicked.connect(self.calculate)
        self.display.returnPressed.connect(self.calculate)
        self.buttons['C'].clicked.connect(self.clear_display)
        self.buttons["DEL"].clicked.connect(self.del_display)

    def signal_content(self, connection):
        if "n!" in connection:
            indx = connection.find("n!")
            connection = connection.replace(connection[indx], "")
        if "mod" in connection:
            connection = connection.replace("mod", '%')
        if "x^y" in connection:
            connection = connection.replace("x^y", "**")
        connection_new = self.display.text() + connection
        self.display.setText(connection_new)

    def calculate(self):
        result = Model.evaluate_expression(self, self.display.text())
        self.display.setText(result)

    def clear_display(self):
        self.display.clear()

    def del_display(self):
        text = self.display.text()[:-1]
        self.display.setText(text)
from functools import partial
from src.model.Model import Model
from src.controllers.Functions import mode


class CalculatorController:
    def __init__(self, buttons, display,  *args, **kwargs):
        super(CalculatorController, self).__init__(*args, **kwargs)
        self.buttons = buttons
        self.display = display

    def connect_signals(self):
        for button_text, button_instance in self.buttons.items():
            if button_text not in {"=", "C", "DEL", "1/x"}:
                button_instance.clicked.connect(partial(self.signal_content, button_text))
        self.buttons['='].clicked.connect(self.calculate)
        self.display.returnPressed.connect(self.calculate)
        self.buttons['C'].clicked.connect(self.clear_display)
        self.buttons["DEL"].clicked.connect(self.del_display)
        try:
            self.buttons["1/x"].clicked.connect(self.invert)
        except KeyError:
            pass

    def signal_content(self, connection):
        if "n!" in connection:
            indx = connection.find("n!")
            connection = connection.replace(connection[indx], "")
        if "mod" in connection:
            connection = connection.replace("mod", '%')
        if "x^y" in connection:
            connection = connection.replace("x^y", "**")
        connection_new = self.display.text() + connection
        self.display.setText(connection_new)

    def calculate(self):
        result = Model.evaluate_expression(self, self.display.text())
        self.display.setText(result)

    def clear_display(self):
        self.display.clear()

    def del_display(self):
        text = self.display.text()[:-1]
        self.display.setText(text)

    def invert(self):
        text = self.display.text()
        text = str(1/int(text))
        self.display.setText(text)
