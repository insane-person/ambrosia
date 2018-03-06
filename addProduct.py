import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp, QCoreApplication
from addProductDialog import Ui_Dialog
from dataBase import *

class AddProduct(QDialog, Ui_Dialog):
    def __init__(self, product_name, **kwargs):
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

        self.productName.setText(product_name)
        self.caloricity.setText(str(kwargs.setdefault("caloricity", 0)))
        self.proteins.setText(str(kwargs.setdefault("proteins", 0)))
        self.fats.setText(str(kwargs.setdefault("fats", 0)))
        self.carbohydrate.setText(str(kwargs.setdefault("carbohydrate", 0)))
        self.weightOfPack.setText(str(kwargs.setdefault("pack_weight", 0)))
        self.weightOfPeace.setText(str(kwargs.setdefault("weight_peace", 0)))

        self.show()

    @staticmethod
    def add_method(self):
        print('slot method called.')

        check = False
        if check == True:
            print(1)
        else:
            QCoreApplication.instance().quit()


    @staticmethod
    def del_method(self):

        print('slot method called.')
        # Это пока костыль, что бы закрыть окошко после удаления
        QCoreApplication.instance().quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = AddProduct("Щиии", caloricity=22, proteins=33, weight_peace=35)
    sys.exit(app.exec_())