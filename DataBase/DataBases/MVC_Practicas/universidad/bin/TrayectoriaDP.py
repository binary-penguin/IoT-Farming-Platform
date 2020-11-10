class TrayectoriaDP:

    # Constructores
    def __init__(self):
        self.cursoClave  = ""
        self.cursoNombre = ""
        self.alumnoMatricula   = ""
        self.alumnoNombre = ""
        self.alumnoCarrera = ""

    def __init__(self, datos):

        if(datos == ""):
            self.cursoClave  = ""
            self.cursoNombre = ""
            self.alumnoMatricula   = ""
            self.alumnoNombre = ""
            self.alumnoCarrera = ""
          
        else:
            st = datos.split("_")
            self.cursoClave  = st[0]
            self.cursoNombre = st[1]
            self.alumnoMatricula  = st[2]
            self.alumnoNombre = st[3]
            self.alumnoCarrera = st[4]


    # Accesors (geters)
    def getCursoCLave(self):
        return self.cursoClave

    def getCursoNombre(self):
        return self.cursoNombre

    def getAlumnoMatricula(self):
        return self.alumnoMatricula

    def getAlumnoNombre(self):
        return self.alumnoNombre

    def getAlumnoCarrera(self):
        return self.alumnoCarrera

    # Mutators (seters)
    def setCursoClave(self, cursoClave_):
        self.cursoClave = cursoClave_

    def setCursoNombre(self, cursoNombre_):
        self.cursoNombre = cursoNombre_

    def setAlumnoMatricula(self, alumnoMatricula_):
        self.alumnoMatricula = alumnoMatricula_

    def setAlumnoNombre(self, alumnoNombre_):
        self.alumnoNombre = alumnoNombre_
    
    def setAlumnoCarrera(self, alumnoCarrera_):
        self.alumnoCarrera = alumnoCarrera_

    
    # Metodos
    def toString(self):
        return '{:10}'.format(self.cursoClave) + " " + '{:30}'.format(self.cursoNombre) + \
               " " +'{:10}'.format(self.alumnoMatricula) + " " + \
               '{:20}'.format(self.alumnoNombre) + " " + '{:5}'.format(self.alumnoCarrera)
