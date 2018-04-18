# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(301, 411)
        MainWindow.setMinimumSize(QtCore.QSize(301, 411))
        MainWindow.setMaximumSize(QtCore.QSize(301, 411))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.mouse = QtWidgets.QPushButton(self.centralWidget)
        self.mouse.setGeometry(QtCore.QRect(0, 110, 61, 61))
        self.mouse.setToolTipDuration(0)
        self.mouse.setStyleSheet("QPushButton { background-color: rgb(215, 215, 215); border: 1px solid gray;} "
                                 "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, "
                                 "y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7); }\n")
        self.mouse.setIconSize(QtCore.QSize(16, 16))
        self.mouse.setObjectName("mouse")
        self.pushButton_cross = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_cross.setGeometry(QtCore.QRect(60, 110, 61, 61))
        self.pushButton_cross.setToolTipDuration(0)
        self.pushButton_cross.setStyleSheet("QPushButton { background-color: rgb(215, 215, 215); "
                                            "border: 1px solid gray;\n"
                                            "} QPushButton:pressed { background-color: qlineargradient("
                                            "x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7); }\n")
        self.pushButton_cross.setObjectName("pushButton_cross")
        self.pushButton_rightbracket = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_rightbracket.setGeometry(QtCore.QRect(120, 110, 61, 61))
        self.pushButton_rightbracket.setToolTipDuration(0)
        self.pushButton_rightbracket.setStyleSheet("QPushButton { background-color: rgb(215, 215, 215); "
                                                   "border: 1px solid gray; } QPushButton:pressed { "
                                                   "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, "
                                                   "y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.pushButton_rightbracket.setObjectName("pushButton_rightbracket")
        self.pushButton_leftBracket = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_leftBracket.setGeometry(QtCore.QRect(180, 110, 61, 61))
        self.pushButton_leftBracket.setToolTipDuration(0)
        self.pushButton_leftBracket.setStyleSheet("QPushButton { background-color: rgb(215, 215, 215); "
                                                  "border: 1px solid gray; } QPushButton:pressed { "
                                                  "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, "
                                                  "y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.pushButton_leftBracket.setObjectName("pushButton_leftBracket")
        self.pushButton_two = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_two.setGeometry(QtCore.QRect(60, 290, 61, 61))
        self.pushButton_two.setToolTip("")
        self.pushButton_two.setToolTipDuration(0)
        self.pushButton_two.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                          "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                          "stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.pushButton_two.setObjectName("pushButton_two")
        self.pushButton_power = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_power.setGeometry(QtCore.QRect(180, 170, 61, 61))
        self.pushButton_power.setToolTipDuration(0)
        self.pushButton_power.setStyleSheet("QPushButton { background-color: rgb(215, 215, 215); "
                                            "border: 1px solid gray; } QPushButton:pressed { "
                                            "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, "
                                            "y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.pushButton_power.setObjectName("pushButton_power")
        self.pushButton_three = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_three.setGeometry(QtCore.QRect(120, 290, 61, 61))
        self.pushButton_three.setToolTip("")
        self.pushButton_three.setToolTipDuration(0)
        self.pushButton_three.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                            "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                            "stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.pushButton_three.setObjectName("pushButton_three")
        self.pushButton_one = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_one.setGeometry(QtCore.QRect(0, 290, 61, 61))
        self.pushButton_one.setToolTip("")
        self.pushButton_one.setToolTipDuration(0)
        self.pushButton_one.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed "
                                          "{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                          "stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.pushButton_one.setObjectName("pushButton_one")
        self.pushButton_five = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_five.setGeometry(QtCore.QRect(60, 230, 61, 61))
        self.pushButton_five.setToolTipDuration(0)
        self.pushButton_five.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                           "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                           "stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.pushButton_five.setObjectName("pushButton_five")
        self.pushButton_ln = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_ln.setGeometry(QtCore.QRect(180, 230, 61, 61))
        self.pushButton_ln.setToolTipDuration(0)
        self.pushButton_ln.setStyleSheet("QPushButton { background-color: rgb(215, 215, 215); "
                                         "border: 1px solid gray; } QPushButton:pressed { "
                                         "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                         "stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.pushButton_ln.setObjectName("pushButton_ln")
        self.pushButton_six = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_six.setGeometry(QtCore.QRect(120, 230, 61, 61))
        self.pushButton_six.setToolTipDuration(0)
        self.pushButton_six.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                          "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                          "stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.pushButton_six.setObjectName("pushButton_six")
        self.pushButton_four = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_four.setGeometry(QtCore.QRect(0, 230, 61, 61))
        self.pushButton_four.setToolTipDuration(0)
        self.pushButton_four.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                           "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                           "stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.pushButton_four.setObjectName("pushButton_four")
        self.pushButton_eight = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_eight.setGeometry(QtCore.QRect(60, 170, 61, 61))
        self.pushButton_eight.setToolTipDuration(0)
        self.pushButton_eight.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                            "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                            "stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.pushButton_eight.setObjectName("pushButton_eight")
        self.pushButton_factorial = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_factorial.setGeometry(QtCore.QRect(180, 290, 61, 61))
        self.pushButton_factorial.setToolTipDuration(0)
        self.pushButton_factorial.setStyleSheet("QPushButton { background-color: rgb(215, 215, 215); "
                                                "border: 1px solid gray; } QPushButton:pressed { "
                                                "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                                "stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.pushButton_factorial.setObjectName("pushButton_factorial")
        self.pushButton_nine = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_nine.setGeometry(QtCore.QRect(120, 170, 61, 61))
        self.pushButton_nine.setToolTipDuration(0)
        self.pushButton_nine.setAutoFillBackground(False)
        self.pushButton_nine.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                           "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                           "stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.pushButton_nine.setObjectName("pushButton_nine")
        self.pushButton_seven = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_seven.setGeometry(QtCore.QRect(0, 170, 61, 61))
        self.pushButton_seven.setToolTipDuration(0)
        self.pushButton_seven.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                            "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                            "stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.pushButton_seven.setObjectName("pushButton_seven")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(120, 350, 61, 61))
        self.pushButton_dot.setToolTipDuration(0)
        self.pushButton_dot.setStyleSheet("QPushButton { background-color: rgb(215, 215, 215); "
                                          "border: 1px solid gray; \n"
                                          "} QPushButton:pressed { background-color: qlineargradient("
                                          "x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.pushButton_dot.setAutoDefault(False)
        self.pushButton_dot.setFlat(False)
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_zero = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_zero.setGeometry(QtCore.QRect(0, 350, 121, 61))
        self.pushButton_zero.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                           "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                           "stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.pushButton_zero.setObjectName("pushButton_zero")
        self.pushButton_root = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_root.setGeometry(QtCore.QRect(180, 350, 61, 61))
        self.pushButton_root.setToolTipDuration(0)
        self.pushButton_root.setStyleSheet("QPushButton { background-color: rgb(215, 215, 215); border: "
                                           "1px solid gray; } QPushButton:pressed { "
                                           "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                           "stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.pushButton_root.setObjectName("pushButton_root")
        self.pushButton_division = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_division.setGeometry(QtCore.QRect(240, 110, 61, 61))
        self.pushButton_division.setToolTipDuration(0)
        self.pushButton_division.setObjectName("pushButton_division")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(240, 290, 61, 61))
        self.pushButton_minus.setToolTipDuration(0)
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(240, 230, 61, 61))
        self.pushButton_plus.setToolTipDuration(0)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_equal = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(240, 350, 61, 61))
        self.pushButton_equal.setToolTipDuration(0)
        self.pushButton_equal.setStyleSheet("QPushButton { background-color: rgb(255, 151, 57); color: white; "
                                            "border: 1px solid gray; } QPushButton:pressed { "
                                            "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                            "stop: 0 #FF7832, stop: 1 #FF9739); }")
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.pushButton_multiply = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_multiply.setGeometry(QtCore.QRect(240, 170, 61, 61))
        self.pushButton_multiply.setToolTipDuration(0)
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.mouse_2 = QtWidgets.QLabel(self.centralWidget)
        self.mouse_2.setGeometry(QtCore.QRect(0, 0, 41, 31))
        self.mouse_2.setStyleSheet("QLabel { qproperty-alignment: \'AlignVCenter | AlignRight\'; }")
        self.mouse_2.setText("")
        self.mouse_2.setObjectName("mouse_2")
        self.pushButton_convertor = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_convertor.setGeometry(QtCore.QRect(220, 0, 81, 31))
        self.pushButton_convertor.setStyleSheet("QPushButton { background-color: rgb(215, 215, 215); "
                                                "border: 1px solid gray; } QPushButton:pressed { "
                                                "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                                "stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.pushButton_convertor.setObjectName("pushButton_convertor")
        self.input = QtWidgets.QLineEdit(self.centralWidget)
        self.input.setGeometry(QtCore.QRect(0, 30, 301, 81))
        self.input.setMinimumSize(QtCore.QSize(301, 81))
        self.input.setMaximumSize(QtCore.QSize(301, 81))
        self.input.setStyleSheet("QLineEdit{border: 1px solid gray; }")
        self.input.setObjectName("input")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MerionesCalculator"))
        self.mouse.setToolTip(_translate("MainWindow", "<html><head/><body><p>Delete a character</p></body></html>"))
        self.mouse.setText(_translate("MainWindow", "DEL"))
        self.pushButton_cross.setToolTip(_translate("MainWindow", "<html><head/><body><p>Delete all</p></body></html>"))
        self.pushButton_cross.setText(_translate("MainWindow", "C"))
        self.pushButton_rightbracket.setToolTip(_translate("MainWindow", "<html><head/><body><p>Left bracket"
                                                                         "</p></body></html>"))
        self.pushButton_rightbracket.setText(_translate("MainWindow", "("))
        self.pushButton_leftBracket.setToolTip(_translate("MainWindow", "<html><head/><body><p>Right bracket"
                                                                        "</p></body></html>"))
        self.pushButton_leftBracket.setText(_translate("MainWindow", ")"))
        self.pushButton_two.setText(_translate("MainWindow", "2"))
        self.pushButton_power.setToolTip(_translate("MainWindow", "<html><head/><body><p>Power</p></body></html>"))
        self.pushButton_power.setText(_translate("MainWindow", "^"))
        self.pushButton_three.setText(_translate("MainWindow", "3"))
        self.pushButton_one.setText(_translate("MainWindow", "1"))
        self.pushButton_five.setText(_translate("MainWindow", "5"))
        self.pushButton_ln.setToolTip(_translate("MainWindow", "<html><head/><body><p>Natural logarithm"
                                                               "</p></body></html>"))
        self.pushButton_ln.setText(_translate("MainWindow", "ln"))
        self.pushButton_six.setText(_translate("MainWindow", "6"))
        self.pushButton_four.setText(_translate("MainWindow", "4"))
        self.pushButton_eight.setText(_translate("MainWindow", "8"))
        self.pushButton_factorial.setToolTip(_translate("MainWindow", "<html><head/><body><p>Factorial"
                                                                      "</p></body></html>"))
        self.pushButton_factorial.setText(_translate("MainWindow", "x!"))
        self.pushButton_nine.setText(_translate("MainWindow", "9"))
        self.pushButton_seven.setText(_translate("MainWindow", "7"))
        self.pushButton_dot.setToolTip(_translate("MainWindow", "<html><head/><body><p>Decimal point"
                                                                "</p></body></html>"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_zero.setText(_translate("MainWindow", "0"))
        self.pushButton_root.setToolTip(_translate("MainWindow", "<html><head/><body><p>Square root</p></body></html>"))
        self.pushButton_root.setText(_translate("MainWindow", "√"))
        self.pushButton_division.setToolTip(_translate("MainWindow", "<html><head/><body><p>Division"
                                                                     "</p></body></html>"))
        self.pushButton_division.setStyleSheet(_translate("MainWindow", "QPushButton { background-color: "
                                                                        "rgb(255, 151, 57); color: white; "
                                                                        "border: 1px solid gray; } "
                                                                        "QPushButton:pressed { "
                                                                        "background-color: qlineargradient(x1: 0, "
                                                                        "y1: 0, x2: 0, y2: 1, stop: 0 #FF7832, "
                                                                        "stop: 1 #FF9739); }"))
        self.pushButton_division.setText(_translate("MainWindow", "÷"))
        self.pushButton_minus.setToolTip(_translate("MainWindow", "<html><head/><body><p>Subtraction"
                                                                  "</p></body></html>"))
        self.pushButton_minus.setStyleSheet(_translate("MainWindow", "QPushButton { background-color: "
                                                                     "rgb(255, 151, 57); color: white; "
                                                                     "border: 1px solid gray; } QPushButton:pressed { "
                                                                     "background-color: qlineargradient(x1: 0, y1: 0, "
                                                                     "x2: 0, y2: 1, stop: 0 #FF7832, "
                                                                     "stop: 1 #FF9739); }"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_plus.setToolTip(_translate("MainWindow", "<html><head/><body><p>Addition</p></body></html>"))
        self.pushButton_plus.setStyleSheet(_translate("MainWindow", "QPushButton { background-color: "
                                                                    "rgb(255, 151, 57); color: white; "
                                                                    "border: 1px solid gray; } QPushButton:pressed "
                                                                    "{ background-color: qlineargradient(x1: 0, y1: 0, "
                                                                    "x2: 0, y2: 1, stop: 0 #FF7832, "
                                                                    "stop: 1 #FF9739); }"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_equal.setToolTip(_translate("MainWindow", "<html><head/><body><p>Show result"
                                                                  "</p></body></html>"))
        self.pushButton_equal.setText(_translate("MainWindow", "="))
        self.pushButton_multiply.setToolTip(_translate("MainWindow", "<html><head/><body><p>Multiplication"
                                                                     "</p></body></html>"))
        self.pushButton_multiply.setStyleSheet(_translate("MainWindow", "QPushButton { background-color: "
                                                                        "rgb(255, 151, 57); color: white; "
                                                                        "border: 1px solid gray; } "
                                                                        "QPushButton:pressed { "
                                                                        "background-color: qlineargradient(x1: 0, "
                                                                        "y1: 0, x2: 0, y2: 1, stop: 0 #FF7832, "
                                                                        "stop: 1 #FF9739); }"))
        self.pushButton_multiply.setText(_translate("MainWindow", "*"))
        self.pushButton_convertor.setToolTip(_translate("MainWindow", "<html><head/><body><p>Open unit convertor"
                                                                      "</p></body></html>"))
        self.pushButton_convertor.setText(_translate("MainWindow", "Convertor"))
