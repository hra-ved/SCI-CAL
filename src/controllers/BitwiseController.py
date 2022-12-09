from functools import partial
from src.model.Model import Model


class BitwiseController:
    def __init__(self, buttons, display,  *args, **kwargs):
        super(BitwiseController, self).__init__(*args, **kwargs)
        self.buttons = buttons
        self.display = display

    def connect_signals(self):
        for button_text, button_instance in self.buttons.items():
            if button_text not in {"=", "DEL"}:
                button_instance.clicked.connect(partial(self.signal_content, button_text))
        self.buttons['='].clicked.connect(self.calculate)
        self.display.returnPressed.connect(self.calculate)
        self.buttons["DEL"].clicked.connect(self.del_display)
        self.buttons['C'].clicked.connect(self.clear_display)

    def signal_content(self, connection):
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
