from PyQt5.QtWidgets import *
from ventanas_py.Cuenta import Ui_Form_Cuenta
from Modelo.conexion import DataBAse

import sys,datetime

class Cuentas(QMainWindow):
    
    def __init__(self):
        super(Cuentas,self).__init__()
        self.cuenta_ui=Ui_Form_Cuenta()
        self.cuenta_ui.setupUi(self)
        
        self.db=DataBAse()
        self.table=self.db.getdatos_cuenta()
        
        self.ok= [None for i in range(2)]
       
        self.cuenta_ui.line_Nombre.textChanged.connect(lambda:self.validar_nombre(self.cuenta_ui.line_Nombre))
        self.cuenta_ui.line_cantidad.textChanged.connect(lambda:self.validar_numero(self.cuenta_ui.line_cantidad))
        self.cuenta_ui.btn_ok.clicked.connect(lambda:self.guardar([
            self.cuenta_ui.line_Nombre,
            self.cuenta_ui.line_cantidad,
            self
        ]))
    #========================================
    #   Recorrido de Tablas
    #========================================

        titulos=["cliente","Cantidad","Abonos","Fecha"]
        deudas=self.table
        # deudas=self.table
        self.cuenta_ui.tableWidget.setColumnCount(4)
        self.cuenta_ui.tableWidget.setHorizontalHeaderLabels(titulos)

        #numero de filas
        self.cuenta_ui.tableWidget.setRowCount(len(deudas))
        #conecctar ala funcion
        self.cuenta_ui.tableWidget.cellClicked.connect(lambda: self.mostrarItem)
        #algoritmo para mostrar mostrarItem
        for row in range(len(deudas)):
            for colum in range(len(deudas[row])):
                self.cuenta_ui.tableWidget.setItem(row,colum,QTableWidgetItem(str(deudas[row][colum])))
        

    #=======================================
                #Funciones
    #=======================================
    def mostrar(self):
        self.show()

    def mostrarItem(self,row,column):
        print(self.cuenta_ui.tableWidget.item(row,column).text())
    
    def validar_nombre(self,line):
        if line.text().isalpha() or " " in line.text():
            print("[+] OK")
            line.setStyleSheet("borde 1px solid green")
            self.ok=True
            print("[+]ok")
       
        else:
            print("[-] Fail")
            line.setStyleSheet("borde 1px solid red")
            self.ok=False

    def validar_numero(self, line):
        if line.text().isnumeric() or " " in line.text():
            print("[+] OK")
            line.setStyleSheet("borde 1px solid green")
            self.ok=True
        else:
            print("[-] Fail")
            line.setStyleSheet("borde 1px solid red")
            self.ok=False
     #================================
    #  MSJ
    #================================
    def messager(self):
        mss=QMessageBox()
        mss.setWindowTitle("mensage")
        mss.setText("reguistro exitoso..!")
        mss.setIcon(QMessageBox.Question)
        mss.exec_()


    def guardar(self,obj):

            self.db.update_cuenta(obj[1].text(),obj[0].text(),datetime.datetime.now())
            self.cuenta_ui.line_Nombre.clear()
            self.cuenta_ui.line_cantidad.clear()
            self.close()
            self.messager()
            print("Cuenta Guardada [+]")
        
   
 
        