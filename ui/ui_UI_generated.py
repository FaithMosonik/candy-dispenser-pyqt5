from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 800)  # Increased window size
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.candyDispenser = QGraphicsView(self.centralwidget)
        self.candyDispenser.setObjectName(u"candyDispenser")
        self.candyDispenser.setGeometry(QRect(50, 50, 500, 600))  # Increased size of graphics view
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(600, 100, 150, 40))  # Adjusted button position and size
        self.popButton = QPushButton(self.centralwidget)
        self.popButton.setObjectName(u"popButton")
        self.popButton.setGeometry(QRect(600, 160, 150, 40))  # Adjusted button position and size
        self.peekButton = QPushButton(self.centralwidget)
        self.peekButton.setObjectName(u"peekButton")
        self.peekButton.setGeometry(QRect(600, 220, 150, 40))  # Adjusted button position and size
        self.ifEmptyButton = QPushButton(self.centralwidget)
        self.ifEmptyButton.setObjectName(u"ifEmptyButton")
        self.ifEmptyButton.setGeometry(QRect(600, 340, 150, 40))  # Adjusted button position and size
        self.sizeButton = QPushButton(self.centralwidget)
        self.sizeButton.setObjectName(u"sizeButton")
        self.sizeButton.setGeometry(QRect(600, 280, 150, 40))  # Adjusted button position and size
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuCandy_Dispenser_Simulation = QMenu(self.menubar)
        self.menuCandy_Dispenser_Simulation.setObjectName(u"menuCandy_Dispenser_Simulation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCandy_Dispenser_Simulation.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Candy Dispenser Simulation", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Push", None))
        self.popButton.setText(QCoreApplication.translate("MainWindow", u"Pop", None))
        self.peekButton.setText(QCoreApplication.translate("MainWindow", u"Peek", None))
        self.ifEmptyButton.setText(QCoreApplication.translate("MainWindow", u"Check if empty", None))
        self.sizeButton.setText(QCoreApplication.translate("MainWindow", u"Check Size", None))
        self.menuCandy_Dispenser_Simulation.setTitle(QCoreApplication.translate("MainWindow", u"Candy Dispenser Simulation", None))

