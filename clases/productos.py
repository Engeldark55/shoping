from PyQt5.QtWidgets import *
from ventanas_py.Producto import Ui_Form_Producto
from Modelo.conexion import DataBAse

import sys,datetime


class Productos(QMainWindow):
    def __init__(self):
        super(Productos,self).__init__()
        self.producto_ui=Ui_Form_Producto()
        self.producto_ui.setupUi(self)
        self.conexion=DataBAse()
       
        
        self.ok=[None for i in range(3)]
        self.resultado=0

        #seleccionando line_edit
        self.producto_ui.lineEdit_3.textChanged.connect(lambda: self.Validar(self.producto_ui.lineEdit_3))
        self.producto_ui.lineEdit_2.textChanged.connect(lambda: self.Validar(self.producto_ui.lineEdit_2))
        self.producto_ui.lineEdit.textChanged.connect(lambda: self.Validar(self.producto_ui.lineEdit))
        self.producto_ui.pushButton.clicked.connect(lambda: self.guardar([
            self.producto_ui.lineEdit_3,
            self.producto_ui.lineEdit_2,
            self.producto_ui.lineEdit,
            self
        ]))
        self.producto_ui.pushButton.clicked.connect(lambda: self.messager)
        

    #Eventos:
    def mostrar(self):
        self.show()

    def Validar(self, line):
       
        if line.text().isnumeric() or " " in line.text():
            line.setStyleSheet("borde 1px solid green")
 
        else:
            print("[-] Fail")
            line.setStyleSheet("borde 1px solid red")
        
           

    def guardar(self,obj):
        
        self.conexion.insert_producto(obj[0].text(),obj[1].text(),obj[2].text(),datetime.datetime.now())
        print(f"[+] Registro guardado!")
        self.resultado = 1

        self.producto_ui.lineEdit.clear() 
        self.producto_ui.lineEdit_2.clear() 
        self.producto_ui.lineEdit_3.clear()

        self.close()
        self.messager()
        
        #self.producto_ui.pushButton.clicked.connect(self.close())
     
    def messager(self):
        mss=QMessageBox()
        mss.setWindowTitle("mensage")
        mss.setText("reguistro exitoso..!")
        mss.setIcon(QMessageBox.Question)
        mss.exec_()




