import sys
from PyQt5.QtWidgets import QApplication
from calculator import CalculatorWindow, Convertor

app = QApplication(sys.argv)

calculator = CalculatorWindow()

sys.exit(app.exec_())