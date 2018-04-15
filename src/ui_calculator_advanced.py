# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advanced.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Advanced(object):
    def setupUi(self, Advanced):
        Advanced.setObjectName("Advanced")
        Advanced.resize(443, 272)
        Advanced.setMinimumSize(QtCore.QSize(443, 272))
        Advanced.setMaximumSize(QtCore.QSize(443, 272))
        Advanced.setStyleSheet("QWidget { background-color: rgb(165, 206, 255);} \n"
"\n"
"")
        self.lineEdit = QtWidgets.QLineEdit(Advanced)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 113, 36))
        self.lineEdit.setStyleSheet("QLineEdit{background-color: rgb(255,255,255);}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Advanced)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 110, 113, 36))
        self.lineEdit_2.setStyleSheet("QLineEdit{background-color: rgb(255,255,255);}\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Advanced)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 160, 113, 36))
        self.lineEdit_3.setStyleSheet("QLineEdit{background-color: rgb(255,255,255);}\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Advanced)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 210, 113, 36))
        self.lineEdit_4.setStyleSheet("QLineEdit{background-color: rgb(255,255,255);}\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Advanced)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 160, 113, 36))
        self.lineEdit_5.setStyleSheet("QLineEdit{background-color: rgb(255,255,255);}\n"
"")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Advanced)
        self.lineEdit_6.setGeometry(QtCore.QRect(240, 110, 113, 36))
        self.lineEdit_6.setStyleSheet("QLineEdit{background-color: rgb(255,255,255);}\n"
"")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Advanced)
        self.lineEdit_7.setGeometry(QtCore.QRect(240, 210, 113, 36))
        self.lineEdit_7.setStyleSheet("QLineEdit{background-color: rgb(255,255,255);}\n"
"")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Advanced)
        self.lineEdit_8.setGeometry(QtCore.QRect(240, 60, 113, 36))
        self.lineEdit_8.setStyleSheet("QLineEdit{background-color: rgb(255,255,255);}\n"
"")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label = QtWidgets.QLabel(Advanced)
        self.label.setGeometry(QtCore.QRect(100, 20, 251, 20))
        self.label.setStyleSheet("QLabel{color: rgb(46, 52, 54);font: 75 italic 11pt \"FreeSerif\";font-size:15pt;}\n"
"\n"
"")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Advanced)
        self.comboBox.setGeometry(QtCore.QRect(150, 60, 51, 36))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Advanced)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 110, 51, 36))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(Advanced)
        self.comboBox_3.setGeometry(QtCore.QRect(150, 160, 51, 36))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(Advanced)
        self.comboBox_4.setGeometry(QtCore.QRect(150, 210, 51, 36))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_5 = QtWidgets.QComboBox(Advanced)
        self.comboBox_5.setGeometry(QtCore.QRect(360, 60, 51, 36))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_6 = QtWidgets.QComboBox(Advanced)
        self.comboBox_6.setGeometry(QtCore.QRect(360, 110, 51, 36))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_7 = QtWidgets.QComboBox(Advanced)
        self.comboBox_7.setGeometry(QtCore.QRect(360, 160, 51, 36))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_8 = QtWidgets.QComboBox(Advanced)
        self.comboBox_8.setGeometry(QtCore.QRect(360, 210, 51, 36))
        self.comboBox_8.setObjectName("comboBox_8")

        self.retranslateUi(Advanced)
        QtCore.QMetaObject.connectSlotsByName(Advanced)

    def retranslateUi(self, Advanced):
        _translate = QtCore.QCoreApplication.translate
        Advanced.setWindowTitle(_translate("Advanced", "MerionesConvertor"))
        self.lineEdit.setToolTip(_translate("Advanced", "<html><head/><body><p>Convert weight</p></body></html>"))
        self.lineEdit_2.setToolTip(_translate("Advanced", "<html><head/><body><p>Convert <a name=\"tts_button\"/>length</p></body></html>"))
        self.lineEdit_3.setToolTip(_translate("Advanced", "<html><head/><body><p>Convert time</p></body></html>"))
        self.lineEdit_4.setToolTip(_translate("Advanced", "<html><head/><body><p>Convert temperature</p></body></html>"))
        self.lineEdit_5.setToolTip(_translate("Advanced", "<html><head/><body><p>Convert time</p></body></html>"))
        self.lineEdit_6.setToolTip(_translate("Advanced", "<html><head/><body><p>Convert <a name=\"tts_button\"/>length</p></body></html>"))
        self.lineEdit_7.setToolTip(_translate("Advanced", "<html><head/><body><p>Convert temperature</p></body></html>"))
        self.lineEdit_8.setToolTip(_translate("Advanced", "<html><head/><body><p>Convert weight</p></body></html>"))
        self.label.setText(_translate("Advanced", "Welcome to MerionesConvertor"))

