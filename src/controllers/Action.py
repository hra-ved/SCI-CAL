from functools import partial


class Action:
    def __init__(self, action, display, *args, **kwargs):
        super(Action, self).__init__(*args, **kwargs)
        self.action = action
        self.display = display

    def connect_signals(self):
        for full, part in self.action.items():
            part.triggered.connect(partial(self.signal_content, full))

    def signal_content(self, connection):
        if not "log" in connection and not "(" in connection:
            connection = "(" + connection + ")"
        connection_new = self.display.text() + connection
        self.display.setText(connection_new)
