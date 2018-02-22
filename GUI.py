from PyQt5 import QtWidgets
from PyQt5.Qt import *


# Наследуемся от QMainWindow
class MainWindow(QMainWindow):
    # Переопределяем конструктор класса
    def __init__(self):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))  # Устанавливаем размеры
        self.setWindowTitle("Ambrosia")  # Устанавливаем заголовок окна

        tabs = QTabWidget(self)

        tabs.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        product_table = QTableWidget(self)
        product_table.setRowCount(10)
        product_table.setColumnCount(5)
        product_table.setHorizontalHeaderLabels(['Наименование', 'Калорийность', 'Белки', 'Жиры', 'Углеводы'])

        tab2 = QTextEdit(self)
        tab3 = QTextEdit(self)
        tab4 = QTextEdit(self)

        tabs.addTab(product_table, "Продукты")
        tabs.addTab(tab2, "Блюда")
        tabs.addTab(tab3, "Раскладка")
        tabs.addTab(tab4, "Закупка")

        hbox = QHBoxLayout()
        hbox.addWidget(tabs)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        wid = QWidget(self)
        self.setCentralWidget(wid)

        wid.setLayout(vbox)

        self.show()

class productTable(QTableWidget):
    def __init__(self, args):
        """
            В конструкторе мы делаем всё, что необходимо для запуска нашего приложения, которое
            создаёт QApplication в __init__ методе, затем добваляет наши виджеты и, наконец,
            запускает exec_loop
        """
        QTableWidget.__init__(self, args)

        product_table = QTableWidget()
        product_table.setRowCount(10)
        product_table.setColumnCount(5)
        product_table.setHorizontalHeaderLabels(['Наименование', 'Калорийность', 'Белки', 'Жиры', 'Углеводы'])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())

