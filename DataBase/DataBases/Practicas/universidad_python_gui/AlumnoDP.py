
class AlumnoDP:

    # Constructores
    def __init__(self):
        self.matricula  = ""
        self.nombre = ""
        self.carrera   = ""
        self.plan  = ""
        self.direccion = ""
        self.telefono = ""

    def __init__(self, datos):

        if(datos == ""):
            self.matricula  = ""
            self.nombre = ""
            self.carrera   = ""
            self.plan  = ""
            self.direccion = ""
            self.telefono = ""
        else:
            st = datos.split("_")
            self.matricula  = st[0]
            
            self.nombre = st[1]
            self.carrera   = st[2]
            self.plan  = st[3]
            self.direccion = st[4]
            self.telefono = st[5]

    # Accesors (geters)
    def getMatricula(self):
        return self.matricula

    def getNombre(self):
        return self.nombre

    def getCarrera(self):
        return self.carrera

    def getPlan(self):
        return self.plan

    def getDireccion(self):
        return self.direccion

    def getTelefono(self):
        return self.telefono


    # Mutators (seters)
    def setMatricula(self,matricula_):
        self.matricula = matricula_

    def setNombre(self,nombre_):
        self.nombre = nombre_

    def setCarrera(self,carrera_):
        self.carrera = carrera_

    def setPlan(self,plan_):
        self.plan = plan_
    
    def setDireccion(self,direccion_):
        self.direccion = direccion_

    def setTelefono(self,telefono_):
        self.telefono = telefono_


    
    # Metodos
    def toString(self):
        return '{:10}'.format(self.matricula) + " " + '{:20}'.format(self.nombre)+ " " +'{:5}'.format(self.carrera)+ " " +'{:5}'.format(self.plan) + " " + '{:20}'.format(self.direccion)+ " " +'{:15}'.format(self.telefono) 

    def toStringSql(self):
        print("'"+self.matricula+"','"+self.nombre+"','"+self.carrera+"','"+self.plan +"','"+self.direccion+"','"+self.telefono+"'")
        return "'"+self.matricula+"','"+self.nombre+"','"+self.carrera+"','"+self.plan +"','"+self.direccion+"','"+self.telefono+"'"
