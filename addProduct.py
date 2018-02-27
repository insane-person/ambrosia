import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from addProductDialog import Ui_Dialog


class AddProduct(QDialog, Ui_Dialog):
    def __init__(self):
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

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = AddProduct()
    sys.exit(app.exec_())