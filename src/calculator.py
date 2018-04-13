from PyQt5 import QtWidgets, QtCore
from ui_calculator import Ui_Calculator
from merionesmathlib import MerionesLib

##
# @brief Class that serves as a bridge between GUI and merionesmathlib
#
# Reacts on button presses and either appends the needed number to the calculator display
# or when the "equals" button is pressed, this passes the inputed string to the mathematical
# library which computes the result of the expression and then the ClaculatorWindow shows
# the result on the display
#
class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):

    ##
    # @brief Initializes the calculator
    #
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

    ##
    # @brief Appends the value of just pressed button on the display
    #
    def button_pressed(self):
        button = self.sender()
        expression = self.input.text() + button.text()

        self.input.setText(expression)
        self.input.setFocus(False)

    ##
    # @brief Reacts on keyboard presses
    # @post The application ends if Escape is pressed
    #
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter:
            self.equals_pressed()
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    ##
    # @brief Erases the display
    #
    def erase(self):
        self.input.setText("")

    ##
    # @brief Passes the expression form display to mathlib and shows the result
    #
    def equals_pressed(self):
        try:
            result = MerionesLib.parse_parentheses(self.input.text())
        except ValueError as e:
            result = str(e)
        self.input.setText(result)
        self.input.setFocus(False)
