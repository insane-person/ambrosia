import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp, QCoreApplication
from addProductDialog import Ui_Dialog
from dataBase import *


class AddProduct(QDialog, Ui_Dialog):

    @db_session
    def __init__(self, id=None):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Редактирование продукта")

        regexp_for_int = QRegExp("\d{1,4}[.,]{1,1}\d{0,2}")
        int_validator = QRegExpValidator(regexp_for_int)
        self.caloricity.setValidator(int_validator)
        self.proteins.setValidator(int_validator)
        self.fats.setValidator(int_validator)
        self.carbohydrate.setValidator(int_validator)
        self.weightOfPack.setValidator(int_validator)
        self.weightOfPeace.setValidator(int_validator)

        regexp_name = QRegExp("(\w{1,40}[ ]?)*")
        name_validator = QRegExpValidator(regexp_name)
        self.productName.setValidator(name_validator)

        self.addButton.clicked.connect(self.add_method)
        self.delButton.clicked.connect(self.del_method)
        self.productName.textChanged.connect(self.change_name_edit_color)

        self.caloricity.setText(str(0))
        self.proteins.setText(str(0))
        self.fats.setText(str(0))
        self.carbohydrate.setText(str(0))
        self.weightOfPack.setText(str(0))
        self.weightOfPeace.setText(str(0))

        self.id = id

        if id is not None:
            product = Product[id]

            if product is not None:
                    self.productName.setText(product.name)
                    self.caloricity.setText(str(product.calories))
                    self.proteins.setText(str(product.proteins))
                    self.fats.setText(str(product.fats))
                    self.carbohydrate.setText(str(product.carbohydrates))
                    self.weightOfPack.setText(str(product.weightOfPack))
                    self.weightOfPeace.setText(str(product.weightOfPiece))

        self.show()

    def change_name_edit_color(self):
        self.productName.setStyleSheet("background-color: white")

    def add_method(self):
        if len(self.productName.text()) == 0:
            self.productName.setStyleSheet("background-color: pink")
        else:
            if len(self.caloricity.text()) == 0:
                self.caloricity.setText(str(0))

            if len(self.proteins.text()) == 0:
                self.proteins.setText(str(0))

            if len(self.fats.text()) == 0:
                self.fats.setText(str(0))

            if len(self.carbohydrate.text()) == 0:
                self.carbohydrate.setText(str(0))

            if len(self.weightOfPack.text()) == 0:
                self.weightOfPack.setText(str(0))

            if len(self.weightOfPeace.text()) == 0:
                self.weightOfPeace.setText(str(0))

            try:
                Product[self.id].name = self.productName.text()
            except:
                print("foo")


        # QCoreApplication.instance().quit()

    def del_method(self):
        print('slot method called.')
        # Order[123].delete()
        # Это пока костыль, что бы закрыть окошко после удаления
        QCoreApplication.instance().quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = AddProduct(2)
    sys.exit(app.exec_())