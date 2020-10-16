
import mysql.connector                    
#from mysql.connector import (connection)  # import B correcta

from ClienteDP import ClienteDP

class BancoADjdbc:
    
    def capturar(self, datos):
        resultado=""
        
        try:
            # 1. Abrir el archivo Clientes.txt
            # archivoOut = open("Clientes.txt", "a")
            conexion = mysql.connector.connect(user='root', database='banco')
            print("Conexion exitosa con la BD Bancomer...\n")
            
            # Preparar el string insertCliente con el comando SQL INSERT
            clientedp = ClienteDP(datos)
            
            insertCliente = "INSERT INTO Cliente1 VALUES("+clientedp.toStringSql()+")"
            
            # 2. Almacenar los datos en el archivo
            # archivoOut.write(datos+"\n")
            statement = conexion.cursor()
            statement.execute(insertCliente)
            conexion.commit()
            
            # 3. Cerrar el archivo
            # archivoOut.close()
            statement.close()
            conexion.close()
            
            resultado = "Datos capturados: "+datos
            print(insertCliente+"\n")
        except:
            resultado = "Error en la Captura de Datos del Cliente..."
        
        return resultado


    def consultar(self):
        # 1. Abrir el archivo para leer
        # archivoIn = open("Clientes.txt","r")
        conexion = mysql.connector.connect(user='root',database='banco')
        
        # Preparar el query a la BD y ejecutarlo
        query = "SELECT * FROM Cliente1"
        # query = "SELECT nocta, nombre, tipo, saldo FROM Cliente"
        statement = conexion.cursor()
        statement.execute(query)
        
        # Procesar los datos de la tabla resultante
        datos=""
        clientedp = ClienteDP(datos)
        tupla = statement.fetchone()
        # while tupla is not None:
        while(tupla != None):
            clientedp.setNocta(tupla[0])
            clientedp.setNombre(tupla[1])
            clientedp.setTipo(tupla[2])
            clientedp.setSaldo(tupla[3])
            
            datos = datos + clientedp.toString() + "\n"
            # print(tupla)
            tupla = statement.fetchone()
        
        # 3. Cerrar el archivo
        # archivoIn.close()
        statement.close()
        conexion.close
        
        print(query+"\n")
        
        return datos


    def consultarTipo(self,tipo):
        # 1. Abrir el archivo
        #archivoIn = open("Clientes.txt","r")
        conexion = mysql.connector.connect(user="root", database="banco")
        
        # Preparar query y ejecutarlo
        query = "SELECT * FROM Cliente1 WHERE tipo='"+tipo+"'"
        statement = conexion.cursor()
        statement.execute(query)
        
        # 2. Procesar datos del archivo
        datos = ""
        encontrado = False
        
        # cliente = archivoIn.readline()
        clientedp = ClienteDP(datos)
        tupla = statement.fetchone()
        # while cliente != "":
        while(tupla != None):
            clientedp.setNocta(tupla[0])
            clientedp.setNombre(tupla[1])
            clientedp.setTipo(tupla[2])
            clientedp.setSaldo(tupla[3])
            
            datos = datos + clientedp.toString() + "\n"
            encontrado = True
        
            # cliente = archivoIn.readline()
            tupla = statement.fetchone()
        
        # 3. Cerrar el archivo
        # archivoIn.close
        statement.close()
        conexion.close()
        
        print(query)
        
        #if encontrado == False:
        if (not encontrado):
            datos = "No se localizo el Tipo de cuenta "+tipo

        return datos

    def consultarCta(self,ncta):
        # 1. Abrir el archivo
        # archivoIn = open("Clientes.txt","r")
        conexion = mysql.connector.connect(user="root", database="Banco")
        
        # Preparar query y ejecutarlo
        query = "SELECT * FROM Cliente1 WHERE nocta='"+ncta+"'"
        statement = conexion.cursor()
        statement.execute(query)
        
        # 2. Procesar datos del archivo
        datos = ""
        encontrado = False
       
        # cliente = archivoIn.readline()
        clientedp = ClienteDP(datos)
        tupla = statement.fetchone()
        # while (cliente != "" and not encontrado):
        if(tupla is not None):
        # if (tupla != None):
            # st = cliente.split("_")
            clientedp.setNocta(tupla[0])
            clientedp.setNombre(tupla[1])
            clientedp.setTipo(tupla[2])
            clientedp.setSaldo(tupla[3])
            
            datos = datos + clientedp.toString() + "\n"
            encontrado = True
            
            # cliente = archivoIn.readline()
        
        # 3. Cerrar el archivo
        # archivoIn.close
        statement.close()
        conexion.close()
        
        print(query)
        
        #if encontrado == False:
        if (not encontrado):
            datos = "No se localizo el Cliente con Cuenta "+ncta
        
        return datos


