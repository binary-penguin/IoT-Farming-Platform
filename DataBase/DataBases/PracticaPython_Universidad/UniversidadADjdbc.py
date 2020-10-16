
import mysql.connector        
import subprocess

from AlumnoDP import AlumnoDP
from CursaDP import CursaDP
from CursoDP import CursoDP

class UniversidadADjdbc:
    
    command = ""

    def capturar(self, datos, op):
        resultado=""
        
        try:
            # 1. Abrir el archivo Clientes.txt
            # archivoOut = open("Clientes.txt", "a")
            conexion = mysql.connector.connect(host = "localhost", port = "3306", user = "root", password = "", database = 'universidad')           

            if op == "ALUMNO":
            # Preparar el string insertCliente con el comando SQL INSERT
                alumnodp = AlumnoDP(datos)
                insert = "INSERT INTO Alumno VALUES("+alumnodp.toStringSql()+")"
            
            if op == "CURSA":
            # Preparar el string insertCursa con el comando SQL INSERT
                cursadp = CursaDP(datos)
                insert = "INSERT INTO Cursa VALUES("+cursadp.toStringSql()+")"

            if op == "CURSO":
            # Preparar el string insertCurso con el comando SQL INSERT
                cursodp = CursoDP(datos)
                insert = "INSERT INTO Curso VALUES("+cursodp.toStringSql()+")"
            
            # 2. Almacenar los datos en el archivo
            # archivoOut.write(datos+"\n")
            statement = conexion.cursor()
            statement.execute(insert)
            conexion.commit()
            
            # 3. Cerrar el archivo
            # archivoOut.close()
            statement.close()
            conexion.close()
            
            resultado = "Datos capturados: "+datos
            print(insert+"\n")
        except:
            resultado = "Error en la Captura de Datos REVISE LOS CAMPOS..."
        
        return resultado

    def consultar(self, op):
        # 1. Abrir el archivo para leer
        # archivoIn = open("Clientes.txt","r")
        conexion = mysql.connector.connect(host = "localhost", port = "3306", user = "root", password = "", database = 'universidad')
        # Preparar el query a la BD y ejecutarlo


        query = "SELECT * FROM " + op
        # query = "SELECT nocta, nombre, tipo, saldo FROM Cliente"
        statement = conexion.cursor()
        statement.execute(query)
        
        # Procesar los datos de la tabla resultante
        datos = ""
        alumnodp = AlumnoDP(datos)
        cursadp = CursaDP(datos)
        cursodp = CursoDP(datos)


        tupla = statement.fetchone()
        # while tupla is not None:
        while(tupla != None):

            if op == "ALUMNO":
                alumnodp.setMatricula(tupla[0])
                alumnodp.setNombre(tupla[1])
                alumnodp.setCarrera(tupla[2])
                alumnodp.setPlan(tupla[3])
                alumnodp.setDireccion(tupla[4])
                alumnodp.setTelefono(tupla[5])

                datos = datos + alumnodp.toString() + "\n"

            if op == "CURSA":
                cursadp.setMatricula(tupla[0])
                cursadp.setCveCurso(tupla[1])
                cursadp.setGrupo(tupla[2])
                cursadp.setSalon(tupla[3])
                cursadp.setHorario(tupla[4])

                datos = datos + cursadp.toString() + "\n"            
            
            if op == "CURSO":
                cursodp.setCveCurso(tupla[0])
                cursodp.setNombre(tupla[1])
                cursodp.setSemestre(tupla[2])
                datos = datos + cursodp.toString() + "\n" 

            tupla = statement.fetchone()
        # 3. Cerrar la base de datos
        statement.close()
        conexion.close

        print(query+"\n")        
        return datos

    def consultarMat(self, matricula):
        # 1. Abrir el archivo
        #archivoIn = open("Clientes.txt","r")
        conexion = mysql.connector.connect(user="root", database="universidad")
        
        # Preparar query y ejecutarlo
        query = "SELECT * FROM Alumno WHERE matricula='"+matricula+"'"
        statement = conexion.cursor()
        statement.execute(query)
        
        # 2. Procesar datos del archivo
        datos = ""
        encontrado = False
        
        # cliente = archivoIn.readline()
        alumnodp = AlumnoDP(datos)
        tupla = statement.fetchone()
        # while cliente != "":
        while(tupla != None):
            alumnodp.setMatricula(tupla[0])
            alumnodp.setNombre(tupla[1])
            alumnodp.setCarrera(tupla[2])
            alumnodp.setPlan(tupla[3])
            alumnodp.setDireccion(tupla[4])
            alumnodp.setTelefono(tupla[5])
            
            datos = datos + alumnodp.toString() + "\n"
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
            datos = "No se localizo la matrícula "+matricula

        return datos

    def consultarCar(self,carrera):
        # 1. Abrir el archivo
        # archivoIn = open("Clientes.txt","r")
        conexion = mysql.connector.connect(user="root", database="Universidad")
        
        # Preparar query y ejecutarlo
        query = "SELECT * FROM Alumno WHERE carrera='"+carrera+"'"
        statement = conexion.cursor()
        statement.execute(query)
        
        # 2. Procesar datos del archivo
        datos = ""
        encontrado = False
       
        # cliente = archivoIn.readline()
        alumnodp = AlumnoDP(datos)
        tupla = statement.fetchone()
        # while cliente != "":
        while(tupla != None):
            alumnodp.setMatricula(tupla[0])
            alumnodp.setNombre(tupla[1])
            alumnodp.setCarrera(tupla[2])
            alumnodp.setPlan(tupla[3])
            alumnodp.setDireccion(tupla[4])
            alumnodp.setTelefono(tupla[5])
            
            datos = datos + alumnodp.toString() + "\n"
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
            datos = "No se localizo el Alumnos con Carrera "+carrera
        
        return datos
    
    def runSubprocess(self, command):
        subprocess.Popen(command)
    
    def consultarCveCurso(self, cveCurso):
        # 1. Abrir el archivo
        #archivoIn = open("Clientes.txt","r")
        conexion = mysql.connector.connect(user="root", database="universidad")
        
        # Preparar query y ejecutarlo
        query = "SELECT * FROM Curso WHERE clave='"+cveCurso+"'"
        statement = conexion.cursor()
        statement.execute(query)
        
        # 2. Procesar datos del archivo
        datos = ""
        encontrado = False
        
        # cliente = archivoIn.readline()
        cursodp = CursoDP(datos)
        tupla = statement.fetchone()
        # while cliente != "":
        while(tupla != None):
            cursodp.setCveCurso(tupla[0])
            cursodp.setNombre(tupla[1])
            cursodp.setSemestre(tupla[2])
            
            datos = datos + cursodp.toString() + "\n" 
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
            datos = "No se localizo el curso con esa clave "+cveCurso

        return datos

    def on_closing(self):
        if messagebox.askokcancel(message="¿Está seguro que quiera salir?", title="MIT DataBase Manager"):
            self.universidad.runSubprocess("mysqladmin -u root shutdown")
            print("Cierre de DataBase exitosa.")
            self.window.destroy()