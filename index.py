#importacion QT5
from os import read
from PyQt5.QtWidgets import *
import sys
#importacion de clases
from ventanas_py.Main import Ui_Form_Main
from clases.productos import Productos
from clases.Gastos import Gastos
from clases.Cuentas import Cuentas
from clases.Ventas import Ventas

#Database
from Modelo.conexion import DataBAse


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.Main_ui=Ui_Form_Main()
        self.Main_ui.setupUi(self)
        #DataBAse
        self.db=DataBAse()
        self.gastos=self.db.getdata_Gastos()
        self.product=self.db.getdata_Producto()
        self.cuentas=self.db.getdatos_cuenta()
        self.venta=self.db.getdatos_ventas()

        
    #========================================
    #  carga de las clases o ventanas
    #========================================
        self.view_producto=Productos()
        self.view_Gasto=Gastos()
        self.view_Cuenta=Cuentas()
        self.view_venta=Ventas()

    #========================================
    #  Botones de las demas ventanas
    #========================================
        self.Main_ui.btn_Producto.clicked.connect(lambda: self.view_producto.mostrar())
        self.Main_ui.btn_Gasto.clicked.connect(lambda: self.view_Gasto.mostrar())
        self.Main_ui.btn_Cuenta.clicked.connect(lambda:self.view_Cuenta.mostrar())
        self.Main_ui.btn_Venta.clicked.connect(lambda: self.view_venta.mostrar())
        self.Main_ui.btn_refrescar.clicked.connect(lambda: self.mostrar_producto)

    #========================================
    #   Radio Buttons
    #========================================
        self.Main_ui.radio_Producto.toggled.connect(lambda: self.mostrar_producto())
        self.Main_ui.radio_Gasto.toggled.connect(lambda: self.mostrar_gastos())
        self.Main_ui.radio_Cuentas.toggled.connect(lambda: self.mostrar_cuentas())
        self.Main_ui.radio_Ventas.toggled.connect(lambda: self.mostrar_ventas())

    #========================================
    #   Recorrido de Tablas
    #========================================
    def MustraGeneral(self,titulos,table,num_Collumnas):
        
        self.Main_ui.tableWidget.setColumnCount(num_Collumnas)
        self.Main_ui.tableWidget.setHorizontalHeaderLabels(titulos)
        #numero de filas
        self.Main_ui.tableWidget.setRowCount(len(table))
        #conecctar ala funcion
        self.Main_ui.tableWidget.cellClicked.connect(lambda: self.mostrarItem)
        #algoritmo para mostrar mostrarItem
        for row in range(len(table)):
            for colum in range(len(table[row])):
                self.Main_ui.tableWidget.setItem(row,colum,QTableWidgetItem(str(table[row][colum])))
       
               
    def limpriar(self):
        pass
    #========================================
    #   Muestran las tablas con las consultas
    #========================================
    def mostrar_gastos(self):
       
        self.titulo=["ID","Nombre","costo","descripcion","Fecha"]
        num_colum=5
        gastto=self.gastos
        #columnas numero
        self.MustraGeneral(self.titulo,gastto,num_colum)

        
       
    def mostrar_producto(self):
       
        titulos=["ID","Numero","Tripa","Corazon","Fecha"]
        num_colum=5
        productt=self.product
        #columnas numero
        self.MustraGeneral(titulos,productt,num_colum)


    def mostrar_cuentas(self):
       
        titulo=["cliente","Cantidad","abonos","Fecha"]
        num_colum=4
        cuent=self.cuentas
        self.MustraGeneral(titulo,cuent,num_colum)


    def mostrar_ventas(self):
        titulo=["producto","cliente","KG/PZ","$","Total","abono","deuda","Fecha"]
        num_colum=8
        ventas=self.venta
        self.MustraGeneral(titulo,ventas,num_colum)
    #===============================================
    #      LLena la tabla mostrando los items
    #===============================================
    def mostrarItem(self,row,column):
        self.Main_ui.tableWidget.item(row,column).text()

    #========================================
    #   Recargar tablas o refrescar NORA: PENDIENTE!!!!
    #========================================
    """def Actualizar(self):
        self.titulo
        table=self.product
        self.MustraGeneral(self.titulo,table)
"""
if __name__=="__main__":
    app=QApplication(sys.argv)
    miapp=Main()
    miapp.show()
    sys.exit(app.exec_())
   

    