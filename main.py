from ui.ui_generated import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Main(Ui_MainWindow):
    pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
