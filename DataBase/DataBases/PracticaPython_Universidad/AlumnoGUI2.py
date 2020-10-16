#from Tkinter import *   # Package de Python 2.7

import tkinter as tk  # Package de Python 3.7
from tkinter import messagebox # Package para desplegar ventanas
import tkinter.font as tkFont # Package para personalizar tipografías
from PIL import Image, ImageTk
from UniversidadADjdbc import UniversidadADjdbc
from WindowCreator import WindowCreator as wc
from CursoGUI import CursoGUI
from CursaGUI import CursaGUI



class AlumnoGUI:
    # Link entre ADjdbc y GUI
    universidad = UniversidadADjdbc()
    cursogui = CursoGUI()
    cursagui = CursaGUI()
    
    def __init__(self):
        
        # Atributos variables
        self.PATH_IMAGEN = "mitbkg.png"
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
        self.bAcceder = tk.Button()
        self.bAlumnos = tk.Button()
        self.bCursa = tk.Button()
        self.bCurso = tk.Button()
        self.backPagInicio = tk.Button()
        self.backPagTipo = tk.Button()
        
        self.lbMatri  = tk.Label()
        self.tfMatri = tk.Entry() 
        self.lbNombre = tk.Label()
        self.tfNombre = tk.Entry()
        self.lbCarrera   = tk.Label()
        self.tfCarrera   = tk.Entry()
        
        self.lbPlan = tk.Label()
        self.tfPlan  = tk.Entry()

        self.lbDirec  = tk.Label()
        self.tfDirec = tk.Entry()

        self.lbTelef  = tk.Label()
        self.tfTelef  = tk.Entry()
        
        self.bCapturar    = tk.Button()
        self.bConsultar   = tk.Button()
        self.bConsultarTC = tk.Button()
        self.bConsultarNC = tk.Button()
        self.backPagTipo = tk.Button()


        self.yScrollbar = tk.Scrollbar()
        self.taDatos = tk.Text() 

        self.bCaptuDatos = tk.Button()
        self.bConsulta = tk.Button()
        self.bConsultaMat = tk.Button()
        self.bConsultaCarr = tk.Button()


        



        self.tfNombreCurso = tk.Entry()

    ### Métodos para crear ventanas

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
                                command = self.pagAlumnos), 500, 100)

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

    def pagAlumnos(self):

        # Background
        wc.changeBkg(self.windowF, "greyBkg.jpg", 1000, 600)

        # Escoger tipo de captura 
        self.opCaptura = "ALUMNO"
        self.opConsulta = "ALUMNO"

        # Borrar los widgets
        self.destroyer()

        self.lbMatri  = self.windowF.add(tk.Label(self.windowF, text="Matrícula:", justify = tk.LEFT), 400, 100)

        self.tfMatri = self.windowF.add(tk.Entry(self.windowF, width = 20), 510, 100)
                        
        
        self.lbNombre = self.windowF.add(tk.Label(self.windowF, text="Nombre:", justify = tk.LEFT), 400, 120)
        self.tfNombre = self.windowF.add(tk.Entry(self.windowF, width = 20), 510, 120)
        
        self.lbCarrera   = self.windowF.add(tk.Label(self.windowF, text="Carrera:", justify = tk.LEFT), 400, 140)
        self.tfCarrera   = self.windowF.add(tk.Entry(self.windowF, width = 20), 510, 140)
        
        self.lbPlan = self.windowF.add(tk.Label(self.windowF, text="Plan:", justify = tk.LEFT), 400, 160)
        self.tfPlan  = self.windowF.add(tk.Entry(self.windowF, width = 20), 510, 160)

        self.lbDirec  = self.windowF.add(tk.Label(self.windowF, text="Dirección:", justify = tk.LEFT), 400, 180)
        self.tfDirec = self.windowF.add(tk.Entry(self.windowF, width = 20), 510, 180)

        self.lbTelef  = self.windowF.add(tk.Label(self.windowF, text="Teléfono:", justify = tk.LEFT), 400, 200)
        self.tfTelef  = self.windowF.add(tk.Entry(self.windowF, width = 20), 510, 200)



        self.bCaptuDatos = self.windowF.add(tk.Button(self.windowF, 
                                text="Capturar Datos", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                command = self.bCaptuDatosEvent), 100, 250)
        
        self.bConsulta = self.windowF.add(tk.Button(self.windowF, 
                                text="Consultar Datos", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                command = self.bConsultaEvent), 366, 250)
        
        self.bConsultaMat = self.windowF.add(tk.Button(self.windowF, 
                                text="Consultar Matrícula", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                command = self.bConsultaMatEvent), 633, 250)
        
        self.bConsultaCarr = self.windowF.add(tk.Button(self.windowF, 
                                text="Consultar Carrera", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                command = self.bConsultarCarrEvent), 900, 250)
        
        #self.taDatos      = Text(self.pagInicio, width=40, height=10)        
        

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
                                command = self.pagTipo), 35, 550)

        # Correr Página
        self.windowF.pack()
        self.windowF.mainloop()

    ### Métodos para Eventos de Botones
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


    def bConsultaEvent(self):
        self.taDatos.delete("1.0",tk.END)
        datos = self.universidad.consultar(self.opConsulta)

        if datos == "":
            messagebox.showwarning(message="El registro introducido no existe.", title="MIT DataBase Manager")
            return
            
        self.taDatos.insert(tk.END,datos)
    
    def bConsultarCarrEvent(self):
        self.taDatos.delete("1.0",tk.END)
        
        carr = self.tfCarrera.get()
        datos = self.universidad.consultarCar(carr)

        if carr == "":
            messagebox.showwarning(message="Por favor introduzca una Carrera.", title="MIT DataBase Manager")
            return


        if (datos == "No se localizo el Alumnos con Carrera "+carr) and (carr != ""):
            messagebox.showwarning(message="La Carrera " + carr + " no pudo ser localizada.", title="MIT DataBase Manager")
            return

        self.taDatos.insert(tk.END,datos)

    def bConsultaMatEvent(self):

        self.taDatos.delete("1.0",tk.END)
        
        matri = self.tfMatri.get()
        datos = self.universidad.consultarMat(matri)

        if matri == "":
            messagebox.showwarning(message="Por favor introduzca una Matrícula.", title="MIT DataBase Manager")
            return

        if (datos == "No se localizo la matrícula " + matri) and (matri != ""):
            messagebox.showwarning(message="La Matrícula " + matri + " no pudo ser localizada.", title="MIT DataBase Manager")
            return
        self.taDatos.insert(tk.END,datos)


    
   
 
    ### Metodo de lectura de datos en Entries

    def obtenerDatos(self):
        matri  = ""
        nom  = ""
        car = ""
        plan = ""
        dire = ""
        tel = ""


        if self.opCaptura == "ALUMNO":
            matri  = self.tfMatri.get()
            matri = str.upper(matri)
            nom  = self.tfNombre.get()
            nom = str.upper(nom)
            car = self.tfCarrera.get()
            car = str.upper(car)
            plan = self.tfPlan.get()
            plan = str.upper(plan)
            dire = self.tfDirec.get()
            dire = str.upper(dire)
            tel = self.tfTelef.get()
            tel = str.upper(tel)

            datos = matri + "_" + nom + "_" + car + "_" + plan + "_" + dire + "_" + tel
            print(datos)
        
        
        if (matri == "" or nom == "" or car == "" or plan == "" or dire == "" or tel == ""):
            datos = "VACIO"
        return datos

    ### Métodos para controlar protocolos de ventana

    
    def destroyer(self):
        self.bAcceder.destroy()
        self.bAlumnos.destroy()
        self.bCursa.destroy()
        self.bCurso.destroy()
        self.backPagInicio.destroy()
        self.lbMatri.destroy()
        self.tfMatri.destroy()
        self.lbNombre.destroy()
        self.tfNombre.destroy()
        self.lbCarrera.destroy()
        self.tfCarrera.destroy()
        self.lbPlan.destroy()
        self.tfPlan.destroy()
        self.lbDirec.destroy()
        self.tfDirec.destroy()
        self.lbTelef.destroy()
        self.tfTelef.destroy()
        self.bCaptuDatos.destroy()
        self.bConsulta.destroy()
        self.bConsultaMat.destroy()
        self.bConsultaCarr.destroy()
        self.backPagTipo.destroy()
        self.taDatos.destroy()


prog = AlumnoGUI()
prog.pagInicio()

