import sys
from PyQt6.QtWidgets import QApplication, QWidget
from src.views.MainWindow import MainWindow
from src.model.Settings import Settings


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.main(self)

    @staticmethod
    def main(self):
        MainWindow.setup_ui(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Settings().__init__()
    main_app = Main()
    main_app.show()
    app.exec()
