import sys, datetime
from decimal import *
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem,QWidget
from PyQt5 import uic
from form_salida import Ui_form_salida
from PyQt5.QtCore import pyqtRemoveInputHook
from E_producto import E_producto
from E_inventario import E_inventario
from E_movimientos import E_movimiento


class salida(QDialog):
    obj_form = Ui_form_salida()
    lista_producto=[]
    lista_producto_agregados = []

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_salida()
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar)
        self.obj_form.btn_limpiar.clicked.connect(self.limpiar_todo)
        self.obj_form.btn_agregar.clicked.connect(self.agregar)
        self.obj_form.btn_confirmar.clicked.connect(self.confirmar)


    def confirmar(self):
        confirma = QMessageBox.question(self, 'Alerta ', "Esta seguro de dar salida a los productos?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if confirma == QMessageBox.Yes:
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_e_movimiento= E_movimiento()
            obj_e_movimiento.fecha =datetime.datetime.now()

            for item in self.lista_producto_agregados:
                obj_e_movimiento.responsable = self.obj_form.cbx_responsable.currentText()
                obj_e_movimiento.cantidad = self.obj_form.doubleSpinBox.text()
                obj_e_movimiento.id_producto = item.id_producto
                obj_e_movimiento.tipo = "Salida"
                obj_e_movimiento.guardar(obj_e_movimiento)
                obj_e_inventario = E_inventario()
                result = obj_e_inventario.get_inventario_id_producto(item.id_producto)
                if result == False:
                    obj_e_inventario.guardar(item)
                else:
                    #pyqtRemoveInputHook()
                    #import pdb; pdb.set_trace()
                    item.cantidad = Decimal(result.cantidad) - Decimal(item.cantidad.replace(",", "."))
                    item.id_inventario=result.id_inventario
                    obj_e_inventario.actualizar(item)


    def agregar(self):
        obj_e_producto= E_producto()
        producto= obj_e_producto.get_producto_nombre(self.obj_form.cbx_producto.currentText())
        obj_e_inventario=E_inventario()
        obj_e_inventario.cantidad=self.obj_form.doubleSpinBox.text()
        obj_e_inventario.id_producto=producto.id_producto
        self.lista_producto_agregados.append(obj_e_inventario)

        rowPosition = self.obj_form.tw_productos.rowCount()
        self.obj_form.tw_productos.insertRow(rowPosition)
        self.obj_form.tw_productos.setItem(rowPosition, 0, QTableWidgetItem(str(producto.id_producto)))
        self.obj_form.tw_productos.setItem(rowPosition, 1, QTableWidgetItem(producto.nombre))
        self.obj_form.tw_productos.setItem(rowPosition, 2, QTableWidgetItem(str(self.obj_form.doubleSpinBox.text())))
        self.obj_form.tw_productos.setItem(rowPosition, 3, QTableWidgetItem(str(self.obj_form.dateEdit.text())))
        self.obj_form.tw_productos.setItem(rowPosition, 4, QTableWidgetItem(str(self.obj_form.cbx_responsable.currentText())))


    def buscar(self):
        self.limpiar()
        obj_E_producto= E_producto()
        if self.obj_form.lne_nombre_buscar.text() !="":
            self.lista_producto= obj_E_producto.get_producto_nombre_like(self.obj_form.lne_nombre_buscar.text())
            self.llenar_combo()
        elif self.obj_form.lne_codigo_buscar.text() != "":
            self.lista_producto = obj_E_producto.get_producto_codigo_like(self.obj_form.lne_codigo_buscar.text())
            self.llenar_combo()

    def limpiar_todo(self):
        self.limpiar()
        self.obj_form.lne_nombre_buscar.setText("")
        self.obj_form.lne_codigo_buscar.setText("")
        while (self.obj_form.tw_productos.rowCount() > 0):
            self.obj_form.tw_productos.removeRow(0)

    def llenar_combo(self):
        for producto in self.lista_producto:
            self.obj_form.cbx_producto.addItem(producto.nombre)



    def limpiar(self):
        self.obj_form.cbx_producto.clear()


