from PyQt5.QtWidgets import *
from ventanas_py.Gasto import Ui_Form_Gasto
from Modelo.conexion import DataBAse

import sys, datetime


class Gastos(QMainWindow):
    def __init__(self):
        super(Gastos,self).__init__()
        
        self.gasto_ui=Ui_Form_Gasto()
        self.gasto_ui.setupUi(self)

        self.conexion=DataBAse()

        self.ok=[None for i in range(3)]
        self.resultado=0
 

        #selecionar
        self.gasto_ui.lineNombre.textChanged.connect(lambda: self.validar_nombre(self.gasto_ui.lineNombre))
        self.gasto_ui.lineCosto.textChanged.connect(lambda: self.valida_costo(self.gasto_ui.lineCosto))
        self.gasto_ui.textDescripcion.textChanged.connect(lambda: self.valida_dec(self.gasto_ui.textDescripcion))

        #botom
        self.gasto_ui.btnOk.clicked.connect(lambda: self.guardar([
            self.gasto_ui.lineNombre,
            self.gasto_ui.lineCosto,
            self.gasto_ui.textDescripcion,
            self
            
        ]))

        
    def mostrar(self):
        self.show()

    def validar_nombre(self,line):
        if line.text().isalpha() or " " in line.text():
            print("[+] OK")
            line.setStyleSheet("borde 1px solid green")
            self.ok[0]=True
            print(self.ok)
       
        else:
            print("[-] Fail")
            line.setStyleSheet("borde 1px solid red")
    
    def valida_costo(self, line):
        if line.text().isnumeric() or " " in line.text():
            print("[+] OK")
            line.setStyleSheet("borde 1px solid green")
            print(line)
            self.ok[1]=True
            print(self.ok)
        else:
            print("[-] Fail")
            line.setStyleSheet("borde 1px solid red")
        
    def valida_dec(self, line):
         #print(self.gasto_ui.textDescripcion.toPlainText())
        if line.toPlainText().isalnum() or " " in line.toPlainText():
            print("[+] OK")
            line.setStyleSheet("borde 1px solid green")
            self.ok[2]=True
            print(self.ok)
        else:
            print("[-] Fail")
            line.setStyleSheet("borde 1px solid red")
  


    
    def guardar(self, obj):
    
        self.conexion.insert_gasto(obj[0].text(),obj[1].text(),obj[2].toPlainText(),datetime.datetime.now())
        self.gasto_ui.lineNombre.clear()
        self.gasto_ui.lineCosto.clear()
        self.gasto_ui.textDescripcion.clear()
        self.close()
     
        self.messager()
        print("[+] Gasto Guardado")
      
    
        
    def messager(self):
        mss=QMessageBox()
        mss.setWindowTitle("mensage")
        mss.setText("Reguistro exitoso..!")
        mss.setIcon(QMessageBox.Question)
        mss.exec_()

            

       
                
           
           
            

        


           
                

