from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator
from merionesmathlib import MerionesLib

class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):

    firstNumber = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_zero.clicked.connect(self.button_pressed)
        self.pushButton_one.clicked.connect(self.button_pressed)
        self.pushButton_two.clicked.connect(self.button_pressed)
        self.pushButton_three.clicked.connect(self.button_pressed)
        self.pushButton_four.clicked.connect(self.button_pressed)
        self.pushButton_five.clicked.connect(self.button_pressed)
        self.pushButton_six.clicked.connect(self.button_pressed)
        self.pushButton_seven.clicked.connect(self.button_pressed)
        self.pushButton_eight.clicked.connect(self.button_pressed)
        self.pushButton_nine.clicked.connect(self.button_pressed)

        self.pushButton_plus.clicked.connect(self.button_pressed)
        self.pushButton_minus.clicked.connect(self.button_pressed)
        self.pushButton_division.clicked.connect(self.button_pressed)
        self.pushButton_factorial.clicked.connect(self.button_pressed)
        self.pushButton_ln.clicked.connect(self.button_pressed)
        self.pushButton_multiply.clicked.connect(self.button_pressed)
        self.pushButton_power.clicked.connect(self.button_pressed)
        self.pushButton_root.clicked.connect(self.button_pressed)

        self.pushButton_cross.clicked.connect(self.erase)

        self.pushButton_leftBracket.clicked.connect(self.button_pressed)
        self.pushButton_rightbracket.clicked.connect(self.button_pressed)

        self.pushButton_dot.clicked.connect(self.button_pressed)

        self.pushButton_equal.clicked.connect(self.equals_pressed)

        self.pushButton_plus.setCheckable(True)
        self.pushButton_minus.setCheckable(True)
        self.pushButton_multiply.setCheckable(True)
        self.pushButton_division.setCheckable(True)

    def button_pressed(self):
        button = self.sender()
        expression = self.input.text() + button.text()

        self.input.setText(expression)
        self.input.setFocus(False)

    def erase(self):
        self.input.setText("")

    #prepared for implementation, here is where whole equation will be solved
    def equals_pressed(self):
        result = MerionesLib.parse_parentheses(self.input.text())
        self.input.setText(result)
        self.input.setFocus(False)

