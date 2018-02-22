import sys
from PyQt5.QtWidgets import QApplication, QDialog
from mainWindow import Ui_MainWindow

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())