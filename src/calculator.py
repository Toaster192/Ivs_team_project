from PyQt5 import QtWidgets, QtCore
from ui_calculator import Ui_Calculator
from ui_calculator_advanced import Ui_Advanced
from merionesmathlib import MerionesLib
from PyQt5.QtGui import *
import os

##
# @brief Class that serves as a bridge between GUI and merionesmathlib
#
# Reacts on button presses and either appends the needed number to the calculator display
# or when the "equals" button is pressed, this passes the inputed string to the mathematical
# library which computes the result of the expression and then the CalculatorWindow shows
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

        dirname = os.path.dirname(__file__)
        icon = dirname + '/icons8-hamster-50.png'
        pixmap = QPixmap(icon)
        self.mouse_2.resize(50, 30)
        self.mouse_2.move(3,0)
        self.mouse_2.setPixmap(pixmap)

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
        self.mouse.clicked.connect(self.erase_last)

        self.pushButton_leftBracket.clicked.connect(self.button_pressed)
        self.pushButton_rightbracket.clicked.connect(self.button_pressed)

        self.pushButton_dot.clicked.connect(self.button_pressed)

        self.pushButton_equal.clicked.connect(self.equals_pressed)

        self.pushButton_plus.setCheckable(True)
        self.pushButton_minus.setCheckable(True)
        self.pushButton_multiply.setCheckable(True)
        self.pushButton_division.setCheckable(True)

        self.pushButton_convertor.clicked.connect(self.on_button_pressed)

    def on_button_pressed(self):
        self.second = Convertor()
        self.second.show()

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
    # @brief Erases the last character from display
    #
    def erase_last(self):
        expression = self.input.text()
        self.input.setText(expression[:-1])

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

##
# @brief Class that serves as a bridge between GUI and merionesmathlib extra functions
#
# User input number, in dropdown choose units and result is shown in the second box
#
class Convertor(QtWidgets.QMainWindow, Ui_Advanced):

    ##
    # @brief Initializes the convertor window
    #
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.comboBox.addItem("kg")
        self.comboBox.addItem("mg")
        self.comboBox.addItem("g")
        self.comboBox.addItem("lb")
        self.comboBox.addItem("t")

        self.comboBox_2.addItem("km")
        self.comboBox_2.addItem("m")
        self.comboBox_2.addItem("cm")
        self.comboBox_2.addItem("mm")
        self.comboBox_2.addItem("mi")

        self.comboBox_3.addItem("h")
        self.comboBox_3.addItem("min")
        self.comboBox_3.addItem("s")
        self.comboBox_3.addItem("day")

        self.comboBox_4.addItem("C")
        self.comboBox_4.addItem("K")
        self.comboBox_4.addItem("F")

        self.comboBox_5.addItem("kg")
        self.comboBox_5.addItem("mg")
        self.comboBox_5.addItem("g")
        self.comboBox_5.addItem("lb")
        self.comboBox_5.addItem("t")

        self.comboBox_6.addItem("km")
        self.comboBox_6.addItem("m")
        self.comboBox_6.addItem("cm")
        self.comboBox_6.addItem("mm")
        self.comboBox_6.addItem("mi")

        self.comboBox_7.addItem("h")
        self.comboBox_7.addItem("min")
        self.comboBox_7.addItem("s")
        self.comboBox_7.addItem("day")

        self.comboBox_8.addItem("C")
        self.comboBox_8.addItem("K")
        self.comboBox_8.addItem("F")

        self.pushButton.clicked.connect(self.convert)

    def convert(self):
        # weight
        input_value = self.lineEdit.text()
        if input_value != "":
            input_units = self.comboBox.currentText()
            result_units = self.comboBox_5.currentText()
            try:
                result = MerionesLib.convert_weight(float(input_value), result_units, input_units)
            except ValueError as e:
                result = str(e)
            self.label_2.setText(str(result))

        # length
        input_value = self.lineEdit_2.text()
        if input_value != "":
            input_units = self.comboBox_2.currentText()
            result_units = self.comboBox_6.currentText()
            try:
                result = MerionesLib.convert_weight(float(input_value), result_units, input_units)
            except ValueError as e:
                result = str(e)
            self.label_3.setText(str(result))

        # time
        input_value = self.lineEdit_3.text()
        if input_value != "":
            input_units = self.comboBox_3.currentText()
            result_units = self.comboBox_7.currentText()
            try:
                result = MerionesLib.convert_weight(float(input_value), result_units, input_units)
            except ValueError as e:
                result = str(e)
            self.label_4.setText(str(result))

        # temperature
        input_value = self.lineEdit_4.text()
        if input_value != "":
            input_units = self.comboBox_4.currentText()
            result_units = self.comboBox_8.currentText()
            try:
                result = MerionesLib.convert_weight(float(input_value), result_units, input_units)
            except ValueError as e:
                result = str(e)
            self.label_5.setText(str(result))
