import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem,QWidget
from PyQt5 import uic
from form_movimientos import Ui_form_movimientos
from PyQt5.QtCore import pyqtRemoveInputHook
from E_movimientos import E_movimiento
from E_producto import E_producto


class movimiento(QDialog):
    obj_form = Ui_form_movimientos()

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_movimientos()
        self.obj_form.setupUi(self)
        self.obj_form.btn_ordenar.clicked.connect(self.ordenar)
        obj_e_movimientos = E_movimiento()
        lista =obj_e_movimientos.get_movimientos()
        for item in lista:
            obj_e_producto= E_producto()
            obj_producto = obj_e_producto.get_producto_id(item.id_producto)

            rowPosition = self.obj_form.tw_ordenar.rowCount()
            self.obj_form.tw_ordenar.insertRow(rowPosition)

            self.obj_form.tw_ordenar.setItem(rowPosition, 0, QTableWidgetItem(str(item.id_movimiento)))
            self.obj_form.tw_ordenar.setItem(rowPosition, 1, QTableWidgetItem(str(item.tipo)))
            self.obj_form.tw_ordenar.setItem(rowPosition, 2, QTableWidgetItem(str(obj_producto.nombre)))
            self.obj_form.tw_ordenar.setItem(rowPosition, 3, QTableWidgetItem(str(item.cantidad)))
            self.obj_form.tw_ordenar.setItem(rowPosition, 4, QTableWidgetItem(str(item.fecha)))






    def ordenar(self):
        a=1
