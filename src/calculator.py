from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator

class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):

    firstNumber = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_zero.clicked.connect(self.digit_pressed)
        self.pushButton_one.clicked.connect(self.digit_pressed)
        self.pushButton_two.clicked.connect(self.digit_pressed)
        self.pushButton_three.clicked.connect(self.digit_pressed)
        self.pushButton_four.clicked.connect(self.digit_pressed)
        self.pushButton_five.clicked.connect(self.digit_pressed)
        self.pushButton_six.clicked.connect(self.digit_pressed)
        self.pushButton_seven.clicked.connect(self.digit_pressed)
        self.pushButton_eight.clicked.connect(self.digit_pressed)
        self.pushButton_nine.clicked.connect(self.digit_pressed)

        self.pushButton_plus.clicked.connect(self.sign_pressed)
        self.pushButton_equal.clicked.connect(self.sign_pressed)
        self.pushButton_dot.clicked.connect(self.sign_pressed)


        self.pushButton_plus.clicked.connect(self.binary_operation_pressed)

        self.pushButton_equal.clicked.connect(self.equals_pressed)

        self.pushButton_plus.setCheckable(True)
        self.pushButton_minus.setCheckable(True)
        self.pushButton_multiply.setCheckable(True)
        self.pushButton_division.setCheckable(True)

    def digit_pressed(self):
        button = self.sender()

        newInput = format(str(self.input.text() + button.text()))

        self.input.setText(newInput)

    def sign_pressed(self):
        button = self.sender()

        newInput = self.input.text() + button.text()

        self.input.setText(str(newInput))

    def binary_operation_pressed(self):
        button = self.sender()

        self.firstNumber = self.input.text()

        button.setChecked(True)

    #prepared for implementation, here is where whole equation will be solved
    def equals_pressed(self):
        secondNumber = str(self.input.text())

        if self.pushButton_plus.isChecked():
            labelNumber = self.firstNumber + secondNumber
            self.pushButton_plus.setChecked(False)

