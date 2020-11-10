class CursoDP:

    # Constructores
    def __init__(self):
        self.cveCurso  = ""
        self.nombre = ""
        self.semestre   = 0
        self.semestre = str(self.semestre)

    def __init__(self, datos):

        if(datos == ""):
            self.cveCurso  = ""
            self.nombre = ""
            self.semestre   = 0
            self.semestre = str(self.semestre)
          
        else:
            st = datos.split("_")
            self.cveCurso  = st[0]
            self.nombre = st[1]
            self.semestre  = st[2]
           

    # Accesors (geters)
    def getCveCurso(self):
        return self.cveCurso

    def getNombre(self):
        return self.nombre

    def getSemestre(self):
        return self.semestre

    # Mutators (seters)
    def setCveCurso(self, cveCurso_):
        self.cveCurso = cveCurso_

    def setNombre(self,nombre_):
        self.nombre = nombre_

    def setSemestre(self,semestre_):
        self.semestre = semestre_
    
    # Metodos
    def toString(self):
        self.semestre = str(self.semestre)
        return '{:10}'.format(self.cveCurso) + " " + '{:30}'.format(self.nombre)+ " " +'{:7}'.format(self.semestre)

    def toStringSql(self):
        return "'"+self.cveCurso+"','"+self.nombre+"','"+self.semestre+"'"
