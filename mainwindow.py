# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setStyleSheet("background-color: rgb(140, 198, 63);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menuBar.setObjectName("menuBar")
        self.menustock = QtWidgets.QMenu(self.menuBar)
        self.menustock.setObjectName("menustock")
        self.menuInventario = QtWidgets.QMenu(self.menuBar)
        self.menuInventario.setObjectName("menuInventario")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionProductoNuevo = QtWidgets.QAction(MainWindow)
        self.actionProductoNuevo.setObjectName("actionProductoNuevo")
        self.actionStock = QtWidgets.QAction(MainWindow)
        self.actionStock.setObjectName("actionStock")
        self.actionEntrada = QtWidgets.QAction(MainWindow)
        self.actionEntrada.setObjectName("actionEntrada")
        self.actionSalida = QtWidgets.QAction(MainWindow)
        self.actionSalida.setObjectName("actionSalida")
        self.actionProductoBuscar = QtWidgets.QAction(MainWindow)
        self.actionProductoBuscar.setObjectName("actionProductoBuscar")
        self.actionMovimientos = QtWidgets.QAction(MainWindow)
        self.actionMovimientos.setObjectName("actionMovimientos")
        self.actionStock_Actual = QtWidgets.QAction(MainWindow)
        self.actionStock_Actual.setObjectName("actionStock_Actual")
        self.menustock.addAction(self.actionProductoNuevo)
        self.menustock.addAction(self.actionProductoBuscar)
        self.menuInventario.addAction(self.actionEntrada)
        self.menuInventario.addAction(self.actionSalida)
        self.menuInventario.addAction(self.actionMovimientos)
        self.menuInventario.addAction(self.actionStock_Actual)
        self.menuBar.addAction(self.menustock.menuAction())
        self.menuBar.addAction(self.menuInventario.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menustock.setTitle(_translate("MainWindow", "Producto"))
        self.menuInventario.setTitle(_translate("MainWindow", "Inventario"))
        self.actionProductoNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.actionStock.setText(_translate("MainWindow", "Stock"))
        self.actionEntrada.setText(_translate("MainWindow", "Entrada"))
        self.actionSalida.setText(_translate("MainWindow", "Salida"))
        self.actionProductoBuscar.setText(_translate("MainWindow", "Buscar"))
        self.actionMovimientos.setText(_translate("MainWindow", "Movimientos"))
        self.actionStock_Actual.setText(_translate("MainWindow", "Stock Actual"))

