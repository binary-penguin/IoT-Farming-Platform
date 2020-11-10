import mysql.connector
import subprocess  
from AlumnoDP import AlumnoDP
from CursaDP import CursaDP
from CursoDP import CursoDP
from TomaListaDP import TomaListaDP
from TrayectoriaDP import TrayectoriaDP

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
    
    def consultarLista(self, cveCurso, queryType):
        '''
        queryType 0 -> Producto Cartesiano
        queryType 1 -> Join
        '''

        if queryType == 0:
            query = "SELECT Curso.clave, Curso.nombre, Alumno.matricula, Alumno.nombre, Alumno.carrera " +  \
            "FROM Cursa, Curso, Alumno " +  \
            "WHERE Alumno.matricula = Cursa.matricula AND Curso.clave=Cursa.cveCurso AND Curso.clave='" + cveCurso + "'"
        elif queryType == 1:
            query = "SELECT Curso.clave, Curso.nombre, Alumno.matricula, Alumno.nombre, Alumno.carrera " + \
                    "FROM Alumno JOIN Cursa ON Alumno.matricula = Cursa.matricula " + \
                    "JOIN Curso ON (Curso.clave = '" + cveCurso + "' AND Curso.clave = Cursa.cveCurso)"


        # 1. Abrir el archivo
        conexion = mysql.connector.connect(user="root", database="universidad")
        
        # Preparar query y ejecutarlo
        
                
        statement = conexion.cursor()
        statement.execute(query)
        
        # 2. Procesar datos del archivo
        datos = ""
        encontrado = False

        cursodp = TomaListaDP(datos)
        tupla = statement.fetchone()

        while(tupla != None):
            cursodp.setCursoClave(tupla[0])
            cursodp.setCursoNombre(tupla[1])
            cursodp.setAlumnoMatricula(tupla[2])
            cursodp.setAlumnoNombre(tupla[3])
            cursodp.setAlumnoCarrera(tupla[4])
            
            datos = datos + cursodp.toString() + "\n" 
            encontrado = True
        

            tupla = statement.fetchone()
        
        # 3. Cerrar el archivo
        statement.close()
        conexion.close()
        
        print(query)
        
        #if encontrado == False:
        if (not encontrado):
            datos = ""

        return datos

    def consultarTrayectoria(self, matricula, queryType):
        '''
        queryType 0 -> Producto Cartesiano
        queryType 1 -> Join
        '''

        # 1. Abrir el archivo
        conexion = mysql.connector.connect(user="root", database="universidad")
        
        # Preparar query y ejecutarlo
        if (queryType == 0):
            query = "SELECT Curso.clave, Curso.nombre, Alumno.matricula, Alumno.nombre, Alumno.carrera " + \
                "FROM Cursa, Curso, Alumno " + \
                "WHERE  Alumno.matricula = '" + matricula + "'" + "AND Alumno.matricula = Cursa.matricula " + \
                "AND Curso.clave = Cursa.cveCurso"
        elif (queryType == 1):
            query = "SELECT Curso.clave, Curso.nombre, Alumno.matricula, Alumno.nombre, Alumno.carrera " + \
                    "FROM Alumno JOIN Cursa ON (Alumno.matricula  = '" + matricula + "'" + " AND Alumno.matricula = Cursa.matricula)" + \
                    "JOIN Curso ON Curso.clave = Cursa.cveCurso"

        statement = conexion.cursor()
        statement.execute(query)
        
        # 2. Procesar datos del archivo
        datos = ""
        encontrado = False

        trayectoriadp = TrayectoriaDP(datos)
        tupla = statement.fetchone()

        while(tupla != None):
            trayectoriadp.setCursoClave(tupla[0])
            trayectoriadp.setCursoNombre(tupla[1])
            trayectoriadp.setAlumnoMatricula(tupla[2])
            trayectoriadp.setAlumnoNombre(tupla[3])
            trayectoriadp.setAlumnoCarrera(tupla[4])
            
            datos = datos + trayectoriadp.toString() + "\n" 
            encontrado = True
            tupla = statement.fetchone()
        
        # 3. Cerrar el archivo
        statement.close()
        conexion.close()
        
        print(query)
        
        #if encontrado == False:
        if (not encontrado):
            datos = ""

        return datos

    