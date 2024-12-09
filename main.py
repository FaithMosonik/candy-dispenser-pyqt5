import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.ui_UI_generated import Ui_MainWindow
from controllers.dispenser_controller import DispenserController
from controllers.event_handlers import EventHandler

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800, 800)  # Set a fixed window size
        self.dispenser_controller = DispenserController()
        self.event_handler = EventHandler(self, self.dispenser_controller)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

