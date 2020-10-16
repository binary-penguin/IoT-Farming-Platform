class CursaDP:

    # Constructores
    def __init__(self):
        self.matricula  = ""
        self.cveCurso = ""
        self.grupo   = ""
        self.salon  = ""
        self.horario = ""

    def __init__(self, datos):

        if (datos == ""):
            self.matricula  = ""
            self.cveCurso = ""
            self.grupo   = ""
            self.salon  = ""
            self.horario = ""
            
        else:
            st = datos.split("_")
            self.matricula  = st[0]     
            self.cveCurso = st[1]
            self.grupo   = st[2]
            self.salon  = st[3]
            self.horario = st[4]

    # Accesors (geters)
    def getMatricula(self):
        return self.matricula

    def getClave(self):
        return self.cveCurso

    def getGrupo(self):
        return self.grupo

    def getSalon(self):
        return self.salon

    def getHorario(self):
        return self.horario

    # Mutators (seters)
    def setMatricula(self,matricula_):
        self.matricula = matricula_

    def setCveCurso(self,cveCurso_):
        self.cveCurso = cveCurso_

    def setGrupo(self,grupo_):
        self.grupo = grupo_

    def setSalon(self,salon_):
        self.salon = salon_
    
    def setHorario(self,horario_):
        self.horario = horario_

    
    # Metodos
    def toString(self):
        return '{:10}'.format(self.matricula) + " " + '{:10}'.format(self.cveCurso)+ " " +'{:10}'.format(self.grupo)+ " " +'{:10}'.format(self.salon) + " " + '{:10}'.format(self.horario)

    def toStringSql(self):
        return "'"+self.matricula+"','"+self.cveCurso+"','"+self.grupo+"','"+self.salon +"','"+self.horario+"'"
