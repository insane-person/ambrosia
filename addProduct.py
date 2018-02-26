import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from addProductDialog import Ui_Dialog

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)

regexpForInt = QRegExp("\d{1,4}[.,]{1,1}\d{0,2}")


caloricityInt = QRegExpValidator(regexpForInt)
proteinsInt = QRegExpValidator(regexpForInt)
fatsInt = QRegExpValidator(regexpForInt)
carbohydrateInt = QRegExpValidator(regexpForInt)
weightOfPackInt = QRegExpValidator(regexpForInt)
weightOfPeaceInt = QRegExpValidator(regexpForInt)


ui.caloricity.setValidator(caloricityInt)
ui.proteins.setValidator(proteinsInt)
ui.fats.setValidator(fatsInt)
ui.carbohydrate.setValidator(carbohydrateInt)

ui.weightOfPack.setValidator(weightOfPackInt)
ui.weightOfPeace.setValidator(weightOfPeaceInt)

regexpForName = QRegExp("(\w{1,40}[ ]?)*")
nameValidator = QRegExpValidator(regexpForName)
ui.productName.setValidator(nameValidator)

class AddProduct(Ui_Dialog):





if __name__ == '__main__':
    window.show()
    sys.exit(app.exec_())

