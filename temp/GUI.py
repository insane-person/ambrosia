import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindow import Ui_MainWindow
from addproduct import

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())

