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
        Advanced.setStyleSheet("QWidget { background-color: rgb(215, 215, 215);} \n"
"\n"
"")
        self.lineEdit = QtWidgets.QLineEdit(Advanced)
        self.lineEdit.setGeometry(QtCore.QRect(40, 40, 113, 36))
        self.lineEdit.setStyleSheet("QLineEdit{background-color: rgb(255,255,255);}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Advanced)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 90, 113, 36))
        self.lineEdit_2.setStyleSheet("QLineEdit{background-color: rgb(255,255,255);}\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Advanced)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 140, 113, 36))
        self.lineEdit_3.setStyleSheet("QLineEdit{background-color: rgb(255,255,255);}\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Advanced)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 190, 113, 36))
        self.lineEdit_4.setStyleSheet("QLineEdit{background-color: rgb(255,255,255);}\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(Advanced)
        self.label.setGeometry(QtCore.QRect(100, 10, 251, 20))
        self.label.setStyleSheet("QLabel{color: rgb(46, 52, 54);font: 75 italic 11pt \"FreeSerif\";font-size:15pt;}\n"
"\n"
"")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Advanced)
        self.comboBox.setGeometry(QtCore.QRect(160, 40, 51, 36))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Advanced)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 90, 51, 36))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(Advanced)
        self.comboBox_3.setGeometry(QtCore.QRect(160, 140, 51, 36))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(Advanced)
        self.comboBox_4.setGeometry(QtCore.QRect(160, 190, 51, 36))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_2 = QtWidgets.QLabel(Advanced)
        self.label_2.setGeometry(QtCore.QRect(260, 45, 113, 31))
        self.label_2.setStyleSheet("QLabel { qproperty-alignment: \'AlignVCenter | AlignRight\'; border: 1px solid grey; background-color:rgb(211, 215, 207);} ")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Advanced)
        self.label_3.setGeometry(QtCore.QRect(260, 95, 113, 31))
        self.label_3.setStyleSheet("QLabel { qproperty-alignment: \'AlignVCenter | AlignRight\'; border: 1px solid grey; background-color:rgb(211, 215, 207);} ")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Advanced)
        self.label_4.setGeometry(QtCore.QRect(260, 145, 113, 31))
        self.label_4.setStyleSheet("QLabel { qproperty-alignment: \'AlignVCenter | AlignRight\'; border: 1px solid grey; background-color:rgb(211, 215, 207);} ")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Advanced)
        self.label_5.setGeometry(QtCore.QRect(260, 190, 113, 31))
        self.label_5.setStyleSheet("QLabel { qproperty-alignment: \'AlignVCenter | AlignRight\'; border: 1px solid grey; background-color:rgb(211, 215, 207);} ")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Advanced)
        self.pushButton.setGeometry(QtCore.QRect(330, 230, 91, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Advanced)
        QtCore.QMetaObject.connectSlotsByName(Advanced)

    def retranslateUi(self, Advanced):
        _translate = QtCore.QCoreApplication.translate
        Advanced.setWindowTitle(_translate("Advanced", "Form"))
        self.lineEdit.setToolTip(_translate("Advanced", "<html><head/><body><p>Convert weight</p></body></html>"))
        self.lineEdit_2.setToolTip(_translate("Advanced", "<html><head/><body><p>Convert <a name=\"tts_button\"/>length</p></body></html>"))
        self.lineEdit_3.setToolTip(_translate("Advanced", "<html><head/><body><p>Convert time</p></body></html>"))
        self.lineEdit_4.setToolTip(_translate("Advanced", "<html><head/><body><p>Convert temperature</p></body></html>"))
        self.label.setText(_translate("Advanced", "Welcome to MerionesConvertor"))
        self.pushButton.setText(_translate("Advanced", "Convert"))

