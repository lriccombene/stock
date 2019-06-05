import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem,QWidget
from PyQt5 import uic
from form_producto import Ui_form_producto
from PyQt5.QtCore import pyqtRemoveInputHook
from E_producto import E_producto


class producto(QDialog):
    obj_form = Ui_form_producto()
    obj_producto = ""
    id=0


    def __init__(self,id_producto):
        QDialog.__init__(self)
        obj_form= Ui_form_producto()
        self.obj_form.setupUi(self)
        self.obj_form.btn_limpiar.clicked.connect(self.limpiar)
        self.obj_form.btn_guardar.clicked.connect(self.guardar)
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        if int(id_producto) != 0 :
            obj_E_producto= E_producto()
            obj_producto= obj_E_producto.get_producto_id(id_producto)
            self.obj_form.lb_id_codigo.setText(str(self.id))
            self.obj_form.lne_codigo_interno.setText(str(obj_producto.codigo_interno))
            self.obj_form.lne_codigo_producto.setText(str(obj_producto.codigo_producto))
            self.obj_form.lne_nombre.setText(obj_producto.nombre)


    def limpiar(self):
        self.obj_producto =""


    def guardar(self):

        obj_e_producto = E_producto()

        if self.obj_form.lne_codigo_producto.text() == "" and self.obj_form.lne_codigo_interno.text() == "":
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msgBox.setText('Falta ingresar codigo')
            msgBox.exec_()
            return False

        if self.obj_form.lne_nombre.text() == "":
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msgBox.setText('Falta ingresar Nombre')
            msgBox.exec_()
            return False
        existe_nombre = obj_e_producto.get_producto_nombre(self.obj_form.lne_nombre.text())

        if existe_nombre != False:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msgBox.setText('El Nombre ya existe ')
            msgBox.exec_()
            return False

        existe_cod_int = obj_e_producto.get_producto_codigo_interno(self.obj_form.lne_codigo_interno.text())

        if existe_cod_int != False:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msgBox.setText('El Codigo Interno ya existe ')
            msgBox.exec_()
            return False

        if self.obj_form.lne_codigo_interno.text() =="" :
            obj_e_producto.codigo_interno = self.obj_form.lne_codigo_producto.text()
        else:
            obj_e_producto.codigo_interno = self.obj_form.lne_codigo_interno.text()

        if self.obj_form.lne_codigo_producto.text() =="":
            obj_e_producto.codigo_producto = self.obj_form.lne_codigo_interno.text()
        else :
            obj_e_producto.codigo_producto = self.obj_form.lne_codigo_producto.text()

        obj_e_producto.nombre = self.obj_form.lne_nombre.text()
        obj_e_producto.fecha = self.obj_form.dte_fec.text()
        obj_e_producto.descripcion = self.obj_form.lne_descripcion.text()
        obj_e_producto.marca = self.obj_form.lne_marca.text()
        obj_e_producto.categoria = self.obj_form.cbx_categoria.currentText()
        obj_e_producto.lote = self.obj_form.lne_lote.text()
        obj_e_producto.detalle = self.obj_form.text_info.toPlainText()
        obj_e_producto.unidad = self.obj_form.cbx_unidad.currentText()


        obj_e_producto.guardar(obj_e_producto)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Atencion")
        msgBox.setText('Prodeucto se guardo correctamente')
        msgBox.exec_()
