# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_salida.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_salida(object):
    def setupUi(self, form_salida):
        form_salida.setObjectName("form_salida")
        form_salida.resize(873, 553)
        form_salida.setStyleSheet("background-color: rgb(140, 198, 63);")
        self.layoutWidget = QtWidgets.QWidget(form_salida)
        self.layoutWidget.setGeometry(QtCore.QRect(270, 150, 153, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.btn_agregar = QtWidgets.QPushButton(form_salida)
        self.btn_agregar.setGeometry(QtCore.QRect(740, 120, 89, 25))
        self.btn_agregar.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.btn_agregar.setObjectName("btn_agregar")
        self.btn_limpiar = QtWidgets.QPushButton(form_salida)
        self.btn_limpiar.setGeometry(QtCore.QRect(740, 50, 89, 25))
        self.btn_limpiar.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.line_2 = QtWidgets.QFrame(form_salida)
        self.line_2.setGeometry(QtCore.QRect(20, 210, 821, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget_2 = QtWidgets.QWidget(form_salida)
        self.layoutWidget_2.setGeometry(QtCore.QRect(110, 150, 163, 28))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget_2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.doubleSpinBox.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.doubleSpinBox.setMaximum(9999.99)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.layoutWidget_3 = QtWidgets.QWidget(form_salida)
        self.layoutWidget_3.setGeometry(QtCore.QRect(110, 110, 291, 27))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget_3)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.cbx_producto = QtWidgets.QComboBox(self.layoutWidget_3)
        self.cbx_producto.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.cbx_producto.setObjectName("cbx_producto")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cbx_producto)
        self.line = QtWidgets.QFrame(form_salida)
        self.line.setGeometry(QtCore.QRect(20, 90, 821, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn_confirmar = QtWidgets.QPushButton(form_salida)
        self.btn_confirmar.setGeometry(QtCore.QRect(730, 480, 89, 25))
        self.btn_confirmar.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.btn_confirmar.setObjectName("btn_confirmar")
        self.label = QtWidgets.QLabel(form_salida)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(form_salida)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 141, 17))
        self.label_2.setObjectName("label_2")
        self.lne_nombre_buscar = QtWidgets.QLineEdit(form_salida)
        self.lne_nombre_buscar.setGeometry(QtCore.QRect(170, 20, 231, 25))
        self.lne_nombre_buscar.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lne_nombre_buscar.setObjectName("lne_nombre_buscar")
        self.tw_productos = QtWidgets.QTableWidget(form_salida)
        self.tw_productos.setGeometry(QtCore.QRect(30, 230, 801, 241))
        self.tw_productos.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.tw_productos.setAutoScrollMargin(16)
        self.tw_productos.setObjectName("tw_productos")
        self.tw_productos.setColumnCount(5)
        self.tw_productos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_productos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_productos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_productos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_productos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_productos.setHorizontalHeaderItem(4, item)
        self.tw_productos.horizontalHeader().setDefaultSectionSize(195)
        self.btn_buscar = QtWidgets.QPushButton(form_salida)
        self.btn_buscar.setGeometry(QtCore.QRect(740, 20, 89, 25))
        self.btn_buscar.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.btn_buscar.setObjectName("btn_buscar")
        self.lne_codigo_buscar = QtWidgets.QLineEdit(form_salida)
        self.lne_codigo_buscar.setGeometry(QtCore.QRect(170, 50, 231, 25))
        self.lne_codigo_buscar.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lne_codigo_buscar.setObjectName("lne_codigo_buscar")
        self.cbx_responsable = QtWidgets.QComboBox(form_salida)
        self.cbx_responsable.setGeometry(QtCore.QRect(185, 185, 213, 25))
        self.cbx_responsable.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.cbx_responsable.setObjectName("cbx_responsable")
        self.cbx_responsable.addItem("")
        self.cbx_responsable.addItem("")
        self.cbx_responsable.addItem("")
        self.label_7 = QtWidgets.QLabel(form_salida)
        self.label_7.setGeometry(QtCore.QRect(85, 185, 101, 26))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(form_salida)
        QtCore.QMetaObject.connectSlotsByName(form_salida)

    def retranslateUi(self, form_salida):
        _translate = QtCore.QCoreApplication.translate
        form_salida.setWindowTitle(_translate("form_salida", "Salida"))
        self.label_6.setText(_translate("form_salida", "Fecha  :"))
        self.btn_agregar.setText(_translate("form_salida", "Agregar"))
        self.btn_limpiar.setText(_translate("form_salida", "Limpiar"))
        self.label_5.setText(_translate("form_salida", "Cantidad :"))
        self.label_3.setText(_translate("form_salida", "Producto :"))
        self.btn_confirmar.setText(_translate("form_salida", "Confirmar"))
        self.label.setText(_translate("form_salida", "Producto Nombre :"))
        self.label_2.setText(_translate("form_salida", "Producto Codigo :"))
        item = self.tw_productos.horizontalHeaderItem(0)
        item.setText(_translate("form_salida", "id"))
        item = self.tw_productos.horizontalHeaderItem(1)
        item.setText(_translate("form_salida", "Producto"))
        item = self.tw_productos.horizontalHeaderItem(2)
        item.setText(_translate("form_salida", "Cantidad"))
        item = self.tw_productos.horizontalHeaderItem(3)
        item.setText(_translate("form_salida", "fecha"))
        item = self.tw_productos.horizontalHeaderItem(4)
        item.setText(_translate("form_salida", "Responsable"))
        self.btn_buscar.setText(_translate("form_salida", "Buscar"))
        self.cbx_responsable.setItemText(0, _translate("form_salida", "Loberia"))
        self.cbx_responsable.setItemText(1, _translate("form_salida", "Pozo Salado"))
        self.cbx_responsable.setItemText(2, _translate("form_salida", "Pedro Inda"))
        self.label_7.setText(_translate("form_salida", "Responsable :"))

