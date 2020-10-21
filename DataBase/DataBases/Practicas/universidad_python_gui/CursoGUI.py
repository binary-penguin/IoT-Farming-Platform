import tkinter as tk  # Package de Python 3.7
from tkinter import messagebox # Package para desplegar ventanas
import tkinter.font as tkFont # Package para personalizar tipografías
from PIL import Image, ImageTk
from UniversidadADjdbc import UniversidadADjdbc
from WindowCreator import WindowCreator as wc 
from CursaGUI import CursaGUI
import subprocess

class CursoGUI:
    # Link entre ADjdbc y GUI
    universidad = UniversidadADjdbc()
    cursagui = CursaGUI()

    def __init__(self):
        
        # Atributos variables
        self.PATH_IMAGEN = "greyBkg.jpg"
        self.ANCHO = 1000
        self.ALTURA = 600
        
        # Atributos de Tk()
        self.window = tk.Tk()
        self.window.title("MIT DataBase Manager")
        self.window.iconbitmap("C:\\Users\\jafp0\\OD\\Second_Year\\DataBase\\DataBases\\PracticaPython_Universidad\\media\\icono.ico")
        self.window.geometry('{}x{}'.format(self.ANCHO, self.ALTURA))
            
        # Declarar protocolos (links entre ventana events y script) parte de Tk()
        self.window.protocol("WM_DELETE_WINDOW", self.universidad.on_closing)

        # Atributos de WindowsMaker()
        self.windowF = wc(self.window, self.PATH_IMAGEN, self.ANCHO, self.ALTURA)

        # Definir tipos de consulta y captura
        self.opCaptura = ""
        self.opConsulta = ""

        # Definir todos los widgets (botones, texto)



        ## PAG INICIO Y TIPO

        self.bAcceder = tk.Button()
        self.bAlumnos = tk.Button()
        self.bCursa = tk.Button()
        self.bCurso = tk.Button()
        self.backPagInicio = tk.Button()
        self.backPagTipo = tk.Button()
        ##

        self.lbNombre = tk.Label()
        self.tfNombre = tk.Entry()

        self.lbClave = tk.Label()
        self.tfClave = tk.Entry()

        self.tfSemestre = tk.Entry()
        self.lbSemestre = tk.Label()

        self.bCaptuDatosCurso = tk.Button()
        self.bConsultaCurso = tk.Button()
        self.bConsultaCveCurso = tk.Button()

        

    def pagInicio(self):

        # Borrar los widgets
        self.destroyer()

        # Background
        wc.changeBkg(self.windowF, "mitbkg.png", 1000, 600)

        # Iniciar Server Mysqld
        self.universidad.runSubprocess("mysqld --explicit_defaults_for_timestamp")
        print("Conexión a MIT DataBase exitosa.")

        # Botones
        self.bAcceder = self.windowF.add(tk.Button(self.windowF, 
                                text="Acceder", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "1",
                                bd = "3",
                                command = self.pagTipo), 500, 250)

        # Texto
        self.textAcceder = self.windowF.canvas.create_text(505,150, fill="white",
                                text="Bienvenido",
                                justify = tk.CENTER,
                                font = self.windowF.fontStyle)
        
        # Correr
        self.windowF.pack()
        self.windowF.mainloop()

    def pagTipo(self):

        # Destroy previous button

        self.destroyer()

        # Background
        wc.changeBkg(self.windowF, "tipobkg.png", 1000, 600)

        # Botones

        self.bAlumnos = self.windowF.add(tk.Button(self.windowF, 
                                text="Revisar Alumnos", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font = self.windowF.fontStyle2,
                                command = self.goAlumnoGui), 500, 100)

        self.bCursa = self.windowF.add(tk.Button(self.windowF, 
                                text="Revisar Cursa", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font = self.windowF.fontStyle2,
                                command = self.cursagui.pagCursa), 500, 250)

        self.bCurso = self.windowF.add(tk.Button(self.windowF, 
                                text="Revisar Curso", 
                                anchor = tk.CENTER,
                                justify = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font = self.windowF.fontStyle2,
                                command = self.cursogui.pagCurso), 500, 400)

        self.backPagInicio = self.windowF.add(tk.Button(self.windowF, 
                                text="Atrás", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "1",
                                bd = "3",
                                command = self.pagInicio), 35, 550)

    def pagCurso(self):

        # Background
        wc.changeBkg(self.windowF, "greyBkg.jpg", 1000, 600)

        # Escoger tipo de captura
        self.opCaptura = "CURSO"
        self.opConsulta = "CURSO"

        # Borrar los widgets
        self.destroyer()

        self.lbClave  = self.windowF.add(tk.Label(self.windowF, text="Clave:", justify = tk.LEFT), 400, 100)
        self.tfClave = self.windowF.add(tk.Entry(self.windowF, width = 20), 510, 100)
                        
        self.lbNombre = self.windowF.add(tk.Label(self.windowF, text="Nombre:", justify = tk.LEFT), 400, 120)
        self.tfNombre = self.windowF.add(tk.Entry(self.windowF, width = 20), 510, 120)
        
        self.lbSemestre  = self.windowF.add(tk.Label(self.windowF, text="Semestre:", justify = tk.LEFT), 400, 140)
        self.tfSemestre   = self.windowF.add(tk.Entry(self.windowF, width = 20), 510, 140)


        self.bCaptuDatosCurso = self.windowF.add(tk.Button(self.windowF, 
                                text="Capturar Datos", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                command = self.bCaptuDatosEvent), 755, 250)
        
        self.bConsultaCurso = self.windowF.add(tk.Button(self.windowF, 
                                text="Consultar Datos", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                command = self.bConsultaEvent), 500, 250)
        
        self.bConsultaCveCurso = self.windowF.add(tk.Button(self.windowF, 
                                text="Consultar Clave", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                command = self.bConsultaCveCursoEvent), 245, 250)

        ## Text Box
            #Pend añadir scrollbar
        self.taDatos = self.windowF.add(tk.Text(self.windowF, width = 80, height = 10), 500, 400)
        
        
        ## Boton Atrás
        self.backPagTipo = self.windowF.add(tk.Button(self.windowF, 
                                text="Atrás", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "1",
                                bd = "3",
                                command = self.alumnogui.pagTipo), 35, 550)
        



        # Correr Página
        self.windowF.pack()
        self.windowF.mainloop()

    def bConsultaEvent(self):
        self.taDatos.delete("1.0",tk.END)
        datos = self.universidad.consultar(self.opConsulta)

        if datos == "":
            messagebox.showwarning(message="El registro introducido no existe.", title="MIT DataBase Manager")
            return
            
        self.taDatos.insert(tk.END,datos)

    def bCaptuDatosEvent(self):
        datos = self.obtenerDatos()
        
        self.taDatos.delete("1.0",tk.END)
        resultado = self.universidad.capturar(datos, self.opCaptura)
        
        if datos == "VACIO":
            messagebox.showwarning(message="Algún campo está vacio.", title="MIT DataBase Manager")
            return
        
        if resultado == "Error en la Captura de Datos REVISE LOS CAMPOS..." and datos != "VACIO":
            messagebox.showwarning(message="Error, revise los campos e intente otra vez.", title="MIT DataBase Manager")
            return

        else:
            self.taDatos.insert(tk.END,resultado)


    def bConsultaCveCursoEvent(self):

        self.taDatos.delete("1.0",tk.END)
        
        cveCurso = self.tfClave.get()
        datos = self.universidad.consultarCveCurso(cveCurso)

        if cveCurso == "":
            messagebox.showwarning(message="Introduzca una clave de curso.", title="MIT DataBase Manager")
            return

        if (datos == "No se localizo el curso con esa clave "+cveCurso) and (cveCurso != ""):
            messagebox.showwarning(message="El Curso con Clave " + cveCurso + " no pudo ser localizado.", title="MIT DataBase Manager")
            return
        
        self.taDatos.insert(tk.END,datos)  

    def goAlumnoGui(self):
        subprocess.run("python AlumnoGUI.py")
    def obtenerDatos(self):
        clav = ""
        cnom = ""
        sem = ""
        
        if self.opCaptura == "CURSO":
            clav = self.tfClave.get()
            clav = str.upper(clav)
            cnom = self.tfNombre.get()
            cnom = str.upper(cnom)
            sem = self.tfSemestre.get()
            sem = str.upper(sem)
            datos = clav + "_" + cnom + "_" + sem

        if (clav == "" or cnom == "" or sem == ""):
            datos = "VACIO"
        return datos

    def destroyer(self):

        # INICIO Y TIPO
        self.bAcceder.destroy()
        self.bAlumnos.destroy()
        self.bAlumnos.destroy()
        self.bCursa.destroy()
        self.bCurso.destroy()
        self.backPagInicio.destroy()



        self.lbNombre = tk.Label()
        self.tfNombre = tk.Entry()

        self.tfSemestre = tk.Entry()
        self.lbSemestre = tk.Label()

        self.bCaptuDatosCurso = tk.Button()
        self.bConsultaCurso = tk.Button()
        self.bConsultaCveCurso = tk.Button()

        self.lbClave = tk.Label()
        self.tfClave = tk.Entry()
        self.alumnogui.backPagTipo.destroy()