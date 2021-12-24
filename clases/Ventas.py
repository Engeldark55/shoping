from PyQt5.QtWidgets import *
from ventanas_py.Ventas import Ui_Form_Ventas
from Modelo.conexion import DataBAse

import sys,datetime

class Ventas(QMainWindow):
    def __init__(self):
        super(Ventas, self).__init__()
        self.ventas_ui=Ui_Form_Ventas()
        self.ventas_ui.setupUi(self)

        self.conexion=DataBAse()
         
        self.ok=[None for i in range(2)]
        self.resultado=0
        #================================
        #    seleccionar campos o widgets
        #================================
        #lines
        self.ventas_ui.line_nombre.textChanged.connect(lambda: self.validar_nombre(self.ventas_ui.line_nombre))
        self.ventas_ui.linePrecio.textChanged.connect(lambda:self.valida_costo(self.ventas_ui.linePrecio))
        self.ventas_ui.line_Recivo.textChanged.connect(lambda: self.valida_costo(self.ventas_ui.line_Recivo))
        self.ventas_ui.lineCantidad.textChanged.connect(lambda: self.valida_costo(self.ventas_ui.lineCantidad))
        self.ventas_ui.line_Recivo.textChanged.connect(lambda: self.PagodeCuenta(self.ventas_ui.line_Recivo))

        #radiobutton
        self.ventas_ui.radioTripa.toggled.connect(lambda: self.calcularTripa(self.ventas_ui.lineCantidad,self.ventas_ui.linePrecio,self.ventas_ui.line_nombre))
        self.ventas_ui.radioCorazon.toggled.connect(lambda: self.calcularCorazon(self.ventas_ui.lineCantidad,self.ventas_ui.linePrecio,self.ventas_ui.line_nombre))
     
        #boton
        self.ventas_ui.btnOk.clicked.connect(lambda: self.GuardarVenta(self.tipo,self.cliente,self.C,self.P,self.total,self.pago, self.Int_resta))
    #================================
    #      Muestra ventana
    #================================
    def mostrar(self):
        self.show()
    #================================
    #    validaciones de campos text y num
    #================================
    def validar_nombre(self,line):
        if line.text().isalpha() or " " in line.text():
            print("[+] OK")
            line.setStyleSheet("borde 1px solid green")
            self.ok[0]=True

            #==============================
            # mostrar la deuda atrasada
            #==============================
            R=self.conexion.SelectClienteOne(line.text())
            self.ventas_ui.label_deuda.setText(str(R))
            if R == None:
                cero=0
                self.ventas_ui.label_deuda.setText(str(cero))
        else:
            print("[-] Fail")
            line.setStyleSheet("borde 1px solid red")
    
    def valida_costo(self, line):
        if line.text().isnumeric() or " " in line.text():
            print("[+] OK")
            line.setStyleSheet("borde 1px solid green")
            self.ok[1]=True
        else:
            print("[-] Fail")
            line.setStyleSheet("borde 1px solid red")
       
    def calcularTripa(self,cantidad,precio,nombre_cliente):
       #saca el total de la venta (kg/pz * $ + deusa)
        self.C=int(cantidad.text())
        self.P=int(precio.text())
        suma=self.C * self.P
        cliente=self.conexion.SelectClienteOne(self.ventas_ui.line_nombre.text())
        cuenta=int(cliente[0])
        self.total=cuenta + suma
        self.ventas_ui.label_Total.setText(str(self.total))
        
        self.tipo=1
        self.cliente=nombre_cliente.text()
        if self.cliente == "martin":
            self.cliente = 1
        elif self.cliente =="jaime":
            self.cliente = 2
        elif self.cliente == "memo":
            self.cliente = 3
        elif self.cliente == "juanito":
            self.cliente = 4
        elif self.cliente == "joel":
            self.cliente = 5
        elif self.cliente == "otro":
            self.cliente = 6

        
    
    #==============================
    # Calculo del producto y deuda
    #==============================

    def calcularCorazon(self,cantidad,precio,nombre_cliente):
        #saca el total de la venta (kg/pz * $ + deusa)
        self.calcularTripa(cantidad,precio,nombre_cliente)
        self.tipo=2
           
    #================================
    #    PAGO y CAMBIO
    #================================
    
    def PagodeCuenta(self,pago):
        if pago.text().isnumeric() or " " in pago.text():
            print("[+] OK")
            pago.setStyleSheet("borde 1px solid green")
            self.pago=int(pago.text())
            total=self.total
            self.resta=total - self.pago
            self.ventas_ui.label_Cambio.setText(str(self.resta))
            self.Int_resta=self.resta

    #================================
    #  MSJ
    #================================
    def messager(self):
        mss=QMessageBox()
        mss.setWindowTitle("mensage")
        mss.setText("reguistro exitoso..!")
        mss.setIcon(QMessageBox.Question)
        mss.exec_()


    #================================
    #   Guardar y actualizar 
    #================================
    def GuardarVenta(self,idTipo,idCuenta,cantidad,precio,total,pago,deuda):
        self.conexion.insert_venta(idTipo,idCuenta,cantidad,precio,total,pago,deuda,datetime.datetime.now())

        self.ventas_ui.line_nombre.clear()
        self.ventas_ui.linePrecio.clear()
        self.ventas_ui.line_Recivo.clear()
        self.ventas_ui.lineCantidad.clear()
        self.ventas_ui.line_Recivo.clear()
        self.close()
        self.messager()
        print("[+] venta reguistrada")
        


