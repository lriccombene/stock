# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_stock_actual.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_stock_actual(object):
    def setupUi(self, form_stock_actual):
        form_stock_actual.setObjectName("form_stock_actual")
        form_stock_actual.resize(712, 621)
        form_stock_actual.setStyleSheet("background-color: rgb(140, 198, 63);")
        self.tw_inventario = QtWidgets.QTableWidget(form_stock_actual)
        self.tw_inventario.setGeometry(QtCore.QRect(40, 90, 591, 491))
        self.tw_inventario.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.tw_inventario.setObjectName("tw_inventario")
        self.tw_inventario.setColumnCount(2)
        self.tw_inventario.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_inventario.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_inventario.setHorizontalHeaderItem(1, item)
        self.tw_inventario.horizontalHeader().setDefaultSectionSize(280)
        self.label = QtWidgets.QLabel(form_stock_actual)
        self.label.setGeometry(QtCore.QRect(26, 30, 131, 20))
        self.label.setObjectName("label")
        self.btn_ordenar = QtWidgets.QPushButton(form_stock_actual)
        self.btn_ordenar.setGeometry(QtCore.QRect(430, 30, 89, 25))
        self.btn_ordenar.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.btn_ordenar.setObjectName("btn_ordenar")
        self.cbx_tipo_producto = QtWidgets.QComboBox(form_stock_actual)
        self.cbx_tipo_producto.setGeometry(QtCore.QRect(180, 30, 221, 25))
        self.cbx_tipo_producto.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.cbx_tipo_producto.setObjectName("cbx_tipo_producto")
        self.cbx_tipo_producto.addItem("")
        self.cbx_tipo_producto.addItem("")
        self.cbx_tipo_producto.addItem("")

        self.retranslateUi(form_stock_actual)
        QtCore.QMetaObject.connectSlotsByName(form_stock_actual)

    def retranslateUi(self, form_stock_actual):
        _translate = QtCore.QCoreApplication.translate
        form_stock_actual.setWindowTitle(_translate("form_stock_actual", "Stock Actual"))
        item = self.tw_inventario.horizontalHeaderItem(0)
        item.setText(_translate("form_stock_actual", "Producto"))
        item = self.tw_inventario.horizontalHeaderItem(1)
        item.setText(_translate("form_stock_actual", "Cantidad"))
        self.label.setText(_translate("form_stock_actual", "Ordenar por tipo :"))
        self.btn_ordenar.setText(_translate("form_stock_actual", "Ordenar"))
        self.cbx_tipo_producto.setItemText(0, _translate("form_stock_actual", "Libreria"))
        self.cbx_tipo_producto.setItemText(1, _translate("form_stock_actual", "Autopartes"))
        self.cbx_tipo_producto.setItemText(2, _translate("form_stock_actual", "Almacen"))

