# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_movimientos.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_movimientos(object):
    def setupUi(self, form_movimientos):
        form_movimientos.setObjectName("form_movimientos")
        form_movimientos.resize(862, 555)
        form_movimientos.setStyleSheet("background-color: rgb(140, 198, 63);")
        self.groupBox = QtWidgets.QGroupBox(form_movimientos)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 811, 511))
        self.groupBox.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.groupBox.setObjectName("groupBox")
        self.tw_ordenar = QtWidgets.QTableWidget(self.groupBox)
        self.tw_ordenar.setGeometry(QtCore.QRect(10, 90, 791, 401))
        self.tw_ordenar.setObjectName("tw_ordenar")
        self.tw_ordenar.setColumnCount(5)
        self.tw_ordenar.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_ordenar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_ordenar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_ordenar.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_ordenar.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_ordenar.setHorizontalHeaderItem(4, item)
        self.tw_ordenar.horizontalHeader().setDefaultSectionSize(150)
        self.cbx_ordenar = QtWidgets.QComboBox(self.groupBox)
        self.cbx_ordenar.setGeometry(QtCore.QRect(30, 40, 141, 25))
        self.cbx_ordenar.setObjectName("cbx_ordenar")
        self.cbx_ordenar.addItem("")
        self.cbx_ordenar.addItem("")
        self.cbx_ordenar.addItem("")
        self.btn_ordenar = QtWidgets.QPushButton(self.groupBox)
        self.btn_ordenar.setGeometry(QtCore.QRect(210, 40, 89, 25))
        self.btn_ordenar.setObjectName("btn_ordenar")

        self.retranslateUi(form_movimientos)
        QtCore.QMetaObject.connectSlotsByName(form_movimientos)

    def retranslateUi(self, form_movimientos):
        _translate = QtCore.QCoreApplication.translate
        form_movimientos.setWindowTitle(_translate("form_movimientos", "Movimientos"))
        self.groupBox.setTitle(_translate("form_movimientos", "Movimientos"))
        item = self.tw_ordenar.horizontalHeaderItem(0)
        item.setText(_translate("form_movimientos", "id"))
        item = self.tw_ordenar.horizontalHeaderItem(1)
        item.setText(_translate("form_movimientos", "Tipo"))
        item = self.tw_ordenar.horizontalHeaderItem(2)
        item.setText(_translate("form_movimientos", "Producto"))
        item = self.tw_ordenar.horizontalHeaderItem(3)
        item.setText(_translate("form_movimientos", "Cantidad"))
        item = self.tw_ordenar.horizontalHeaderItem(4)
        item.setText(_translate("form_movimientos", "Fecha"))
        self.cbx_ordenar.setItemText(0, _translate("form_movimientos", "Entrada"))
        self.cbx_ordenar.setItemText(1, _translate("form_movimientos", "Salida"))
        self.cbx_ordenar.setItemText(2, _translate("form_movimientos", "Fecha"))
        self.btn_ordenar.setText(_translate("form_movimientos", "Ordenar"))

