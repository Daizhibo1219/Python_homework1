# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AirconditionWin2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(392, 383)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 371, 311))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.Weather_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.Weather_comboBox.setObjectName("Weather_comboBox")
        self.Weather_comboBox.addItem("")
        self.Weather_comboBox.addItem("")
        self.Weather_comboBox.addItem("")
        self.Weather_comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Weather_comboBox)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(120, 340, 150, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.queary_pushButton = QtWidgets.QPushButton(self.splitter)
        self.queary_pushButton.setObjectName("queary_pushButton")
        self.clearout_pushButton = QtWidgets.QPushButton(self.splitter)
        self.clearout_pushButton.setObjectName("clearout_pushButton")

        self.retranslateUi(Form)
        self.queary_pushButton.clicked.connect(Form.queryAircondition)
        self.clearout_pushButton.clicked.connect(Form.clearResult)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "查询城市空气质量"))
        self.label.setText(_translate("Form", "城市"))
        self.Weather_comboBox.setItemText(0, _translate("Form", "北京"))
        self.Weather_comboBox.setItemText(1, _translate("Form", "上海"))
        self.Weather_comboBox.setItemText(2, _translate("Form", "合肥"))
        self.Weather_comboBox.setItemText(3, _translate("Form", "南京"))
        self.queary_pushButton.setText(_translate("Form", "查询"))
        self.clearout_pushButton.setText(_translate("Form", "清空"))

