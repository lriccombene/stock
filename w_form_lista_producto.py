import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem,QWidget
from PyQt5 import uic
from form_lista_producto import Ui_form_lista_producto
from PyQt5.QtCore import pyqtRemoveInputHook
from E_producto import E_producto
from E_inventario import E_inventario
from w_form_producto import producto


class lista_producto(QDialog):
    obj_form = Ui_form_lista_producto()
    obj_producto = ""
    lista_producto=""
    id=0

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_lista_producto()
        self.obj_form.setupUi(self)
        self.obj_form.btn_nuevo.clicked.connect(self.nuevo)
        self.obj_form.btn_buscar.clicked.connect(self.buscar)
        self.obj_form.btn_limpiar.clicked.connect(self.limpiar)
        self.obj_form.btn_actualizar.clicked.connect(self.actualizar)
        self.obj_form.tw_producto.cellClicked.connect(self.seleccion_item_producto)

        obj_E_producto= E_producto()
        self.lista_producto=obj_E_producto.get_lista_productos()
        self.llenar_grilla()

    def seleccion_item_producto(self,clickedIndex):
        twi0 = self.obj_form.tw_producto.item(clickedIndex, 0)
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        self.id = twi0.text()


    def actualizar(self):

        self.form_producto = producto(self.id)

        self.form_producto.show()


    def buscar(self):
        self.limpiar()
        obj_E_producto= E_producto()
        if self.obj_form.lne_nombre_buscar.text() !="":
            self.lista_producto= obj_E_producto.get_producto_nombre_like(self.obj_form.lne_nombre_buscar.text())
            self.llenar_grilla()
        elif self.obj_form.lne_codigo_buscar.text() != "":
            self.lista_producto = obj_E_producto.get_producto_codigo_like(self.obj_form.lne_codigo_buscar.text())
            self.llenar_grilla()


    def llenar_grilla(self):
        for item in self.lista_producto:
            obj_e_inventario=E_inventario()
            obj_inventario =  obj_e_inventario.get_inventario_id_producto(item.id_producto)
            cantidad=0
            if obj_inventario != False:
                cantidad = obj_inventario.cantidad
            rowPosition = self.obj_form.tw_producto.rowCount()
            self.obj_form.tw_producto.insertRow(rowPosition)

            self.obj_form.tw_producto.setItem(rowPosition, 0, QTableWidgetItem(str(item.id_producto)))
            self.obj_form.tw_producto.setItem(rowPosition, 1, QTableWidgetItem(item.codigo_interno))
            self.obj_form.tw_producto.setItem(rowPosition, 2, QTableWidgetItem(item.nombre))
            self.obj_form.tw_producto.setItem(rowPosition, 3, QTableWidgetItem(item.descripcion))
            self.obj_form.tw_producto.setItem(rowPosition, 4, QTableWidgetItem(str(cantidad)))
            self.obj_form.tw_producto.setItem(rowPosition, 5, QTableWidgetItem(item.codigo_producto))

    def nuevo(self):
        self.form_producto = producto(0)

        self.form_producto.show()

    def limpiar(self):
        self.obj_producto=""
        self.lista_producto =""

        while (self.obj_form.tw_producto.rowCount() > 0):
            self.obj_form.tw_producto.removeRow(0)

