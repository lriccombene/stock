import sys, datetime
from decimal import *
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem,QWidget
from PyQt5 import uic
from form_stock_actual import Ui_form_stock_actual
from PyQt5.QtCore import pyqtRemoveInputHook
from E_producto import E_producto
from E_inventario import E_inventario
from E_movimientos import E_movimiento


class inventario(QDialog):
    obj_form = Ui_form_stock_actual()
    lista_producto=[]
    lista_producto_agregados = []

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_stock_actual()
        self.obj_form.setupUi(self)
        self.obj_form.btn_ordenar.clicked.connect(self.ordenar)
        obj_e_inventario= E_inventario()
        list_inventario= obj_e_inventario.get_inventario()

        for item in list_inventario:

            obj_e_producto = E_producto()
            obj_producto = obj_e_producto.get_producto_id(item.id_producto)

            rowPosition = self.obj_form.tw_inventario.rowCount()
            self.obj_form.tw_inventario.insertRow(rowPosition)

            self.obj_form.tw_inventario.setItem(rowPosition, 0, QTableWidgetItem(str(obj_producto.nombre)))
            self.obj_form.tw_inventario.setItem(rowPosition, 1, QTableWidgetItem(str(item.cantidad)))



    def ordenar(self):
        self.limpiar()
        obj_e_inventario = E_inventario()
        lista_inventario = obj_e_inventario.get_inventario_tipo_prod(self.obj_form.cbx_tipo_producto.currentText())

        for item in lista_inventario:
            rowPosition = self.obj_form.tw_inventario.rowCount()
            self.obj_form.tw_inventario.insertRow(rowPosition)
            self.obj_form.tw_inventario.setItem(rowPosition, 0, QTableWidgetItem(str(item.nombre)))
            self.obj_form.tw_inventario.setItem(rowPosition, 1, QTableWidgetItem(str(item.cantidad)))


    def limpiar(self):

        while (self.obj_form.tw_inventario.rowCount() > 0):
            self.obj_form.tw_inventario.removeRow(0)