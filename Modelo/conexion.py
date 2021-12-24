import sqlite3
import datetime

class DataBAse:
    def __init__(self):
        self.conexion=sqlite3.connect("Modelo/PuntoVentaR.db")
        self.cursor=self.conexion.cursor()
#========================================================
                   # Actualizaer datos
#========================================================
    def update_cuenta(self,abono,cliente,fecha):
        self.cursor.execute(f"UPDATE Cuentas SET cantidad=cantidad-{abono},abono={abono},fecha='{fecha}' WHERE Nombre='{cliente}'")
        self.conexion.commit()
        
#========================================================
                   # Insert DAtos
#========================================================
    def insert_gasto(self,name,costo,desc,fecha):
        self.cursor.execute( f"INSERT INTO Gastos VALUES(NULL,'{name}',{costo},'{desc}','{fecha}')")
        self.conexion.commit()
   
    def insert_producto(self,socio,tripa,corazon,fecha):
       self.cursor.execute( f"INSERT INTO Provedor VALUES(NULL,{socio},{tripa},{corazon},'{fecha}')")
       self.conexion.commit()
 
    def insert_venta(self,idTipo,idCuenta,cantidad,precio,total,pago,deuda,fecha):
        self.cursor.execute(f"INSERT INTO Ventas(id_tipo,id_cuenta,cantidad,precio,total_venta,pago,deuda,fecha) VALUES({idTipo},{idCuenta},{cantidad},{precio},{total},{pago},{deuda},'{fecha}')")
        self.conexion.commit()

#========================================================
                   # MOSTRAR TODOs DATO
#========================================================
    def getdata_Gastos(self):
        self.cursor.execute(f"SELECT * FROM Gastos")
        lis=self.cursor.fetchall()
  
        return lis
    
    def getdata_Producto(self):
        self.cursor.execute(f"SELECT * FROM Provedor")
        lis=self.cursor.fetchall()

        return lis
    def getdata_Ventas(self):
        self.cursor.execute(f"SELECT * FROM Ventas")
        lis=self.cursor.fetchall()
        return lis
    def getdatos_cuenta(self):
        self.cursor.execute("SELECT Nombre,cantidad,abono,fecha FROM Cuentas")
        datoS=self.cursor.fetchall()
        return datoS
    def getdatos_cuenta_cantidad(self):
        self.cursor.execute("SELECT cantidad FROM Cuentas WHERE  Nombre='martin'")
        datoS=self.cursor.fetchall()
        return datoS

    def getdatos_ventas(self):
        self.cursor.execute("""SELECT Tipo.Nombre,Cuentas.Nombre,Ventas.cantidad,Ventas.precio,Ventas.total_venta,Ventas.pago,Ventas.fecha FROM Ventas 
                                INNER JOIN Tipo on Ventas.id_tipo=Tipo.ID 
                                INNER JOIN Cuentas on Ventas.id_cuenta=Cuentas.ID""")
                                
        ventas=self.cursor.fetchall()
        return ventas
    
#========================================================
                   # seleccionar datos
#========================================================
    def nombreCliente(self,nombre):
        self.cursor.execute(f"SELECT {nombre} FROM Cuentas")
        nombre=self.cursor.fetchone()
        return nombre
    def SelectClienteOne(self,name):
        self.cursor.execute(f"SELECT cantidad FROM Cuentas WHERE Nombre='{name}'")
        clienteOne=self.cursor.fetchone()
        return clienteOne
    def getVenta(self):
        self.cursor.execute("SELECT * FROM Ventas")
        datoS=self.cursor.fetchall()
        return datoS
        

