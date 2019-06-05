import sys,datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem,QMainWindow
from mainwindow import Ui_MainWindow
from PyQt5 import uic
from PyQt5.QtCore import pyqtRemoveInputHook

from w_form_producto import producto
from w_form_lista_producto import lista_producto
from w_form_entrada import entrada
from w_form_movimientos import movimiento
from w_form_salida import salida
from w_form_stock_actual import inventario


class Mainwindow(QMainWindow):

    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        self.obj_form_main = Ui_MainWindow()
        self.obj_form_main.setupUi(self)
        self.obj_form_main.actionProductoNuevo.triggered.connect(self.Nuevo_producto)
        self.obj_form_main.actionProductoBuscar.triggered.connect(self.lista_producto)
        self.obj_form_main.actionEntrada.triggered.connect(self.Entrada)
        self.obj_form_main.actionSalida.triggered.connect(self.Salida)
        self.obj_form_main.actionMovimientos.triggered.connect(self.movimientos)
        self.obj_form_main.actionStock_Actual.triggered.connect(self.stock_actual)

    def stock_actual(self):
        self.form_inventario= inventario()
        self.form_inventario.show()

    def Salida(self):
        self.form_salida = salida()
        self.form_salida.show()

    def movimientos(self):
        self.form_movimientos=movimiento()
        self.form_movimientos.show()


    def lista_producto(self):
        self.form_lista_producto = lista_producto()
        self.form_lista_producto.show()

    def Entrada(self):
        self.form_entrada= entrada()
        self.form_entrada.show()

    def Nuevo_producto(self):
        id=0
        self.form_producto = producto(id)
        self.form_producto.show()



app = QApplication(sys.argv)
dialogo= Mainwindow()
dialogo.show()

app.exec_()
