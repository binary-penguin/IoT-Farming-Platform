#!/usr/bin/python
# _*_ coding: utf-8 _*_

import tkinter as tk # STANDARD
from tkinter import messagebox # STANDARD
import tkinter.font as tkFont # STANDARD
import tkinter.scrolledtext as ts # STANDARD
from PIL import Image, ImageTk # NON-STANDARD Allows the use of different image formats
import os # STANDARD
from UniversidadADjdbc import UniversidadADjdbc

# V-I-E-W
# Dynamically renders the GUI

######## TO DO
##### 1. DYNAMICALLY RENDER GUI, using lambdas probably?
##### 2. SENDING BACK TO CONTROLLER DATABASE ACTIONS

# 1. ROOT -> 2. FRAME (background) -> 3. CANVAS (adds Widgets)

''' View Object of Universidad'''


class UniViewR(tk.Tk):
    def __init__(self):
            super().__init__()
            # Atributos CONSTANTES
            self.PATH_BKG = os.path.abspath("assets\\mitbkg.png")
            self.PATH_ICON = os.path.abspath("assets\\icono.ico")
            self.ANCHO = 1000
            self.ALTURA = 600
            
            # Atributos de Tk() 
            self.title("MIT DataBase Manager")
            self.iconbitmap(self.PATH_ICON)
            self.geometry('{}x{}'.format(self.ANCHO, self.ALTURA))

            # Declarar protocolos (links entre ventana events y script) parte de Tk()
            self.protocol("WM_DELETE_WINDOW", self.on_closing)

            # List of FRAME Objects
            self.frame_list = []

            # OPENS MAINPAGE FRAME
            self.universidad = UniversidadADjdbc()
            self.main_page()
            

    def main_page(self):
        self.deleteFrames()
        self.MAIN_PAGE = UniViewF(self, "assets\\mitbkg.png")
        self.MAIN_PAGE.pack_frame(0,0)

        # Entrar Button
        self.MAIN_PAGE.uvc.addWidget(tk.Button(self.MAIN_PAGE.uvc, 
                                    text="Entrar", 
                                    anchor = tk.CENTER,
                                    bg = "#A31F34",
                                    foreground = "white",
                                    width = "18",
                                    height = "1",
                                    bd = "3",
                                    command = self.pagina_tipo), 500, 250)

        # Bienvenido text
        self.MAIN_PAGE.uvc.create_text(505,150, fill="white",
                                        text="Bienvenido",
                                        justify = tk.CENTER,
                                        font = self.MAIN_PAGE.fontStyle)

        # Author text  
        self.MAIN_PAGE.uvc.create_text(870,570, fill="white",
                                        text="Developed by Jorge Flores",
                                        justify = tk.RIGHT,
                                        font = self.MAIN_PAGE.fontStyle3)

        # Add frame to the window list
        self.frame_list.append(self.MAIN_PAGE)


    def pagina_tipo(self):
        super().destroy()
        super().__init__()
        self.deleteFrames()
        self.TIPO_PAGE = UniViewF(self, "assets\\tipobkg.png")
        self.TIPO_PAGE.pack_frame(0,0)

        # Revisar Alumnos Button
        self.TIPO_PAGE.uvc.addWidget(tk.Button(self.TIPO_PAGE.uvc, 
                                text="Revisar Alumnos", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font = self.TIPO_PAGE.fontStyle2,
                                command = self.pagina_alumnos), 350, 125)

        # Revisar Cursa Button
        self.TIPO_PAGE.uvc.addWidget(tk.Button(self.TIPO_PAGE.uvc, 
                                text="Revisar Cursa", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                font = self.TIPO_PAGE.fontStyle2,
                                command = self.pagCursa), 650, 125)

        # Revisar Curso Button
        self.TIPO_PAGE.uvc.addWidget(tk.Button(self.TIPO_PAGE.uvc, 
                                text="Revisar Curso", 
                                anchor = tk.CENTER,
                                justify = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                font = self.TIPO_PAGE.fontStyle2,
                                command = self.pagCurso), 350, 325)
        
        # Reportes Button
        self.TIPO_PAGE.uvc.addWidget(tk.Button(self.TIPO_PAGE.uvc, 
                                text="Reportes", 
                                anchor = tk.CENTER,
                                justify = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                font = self.TIPO_PAGE.fontStyle2,
                                command = self.pagReporte), 650, 325)

        # Atrás button
        self.TIPO_PAGE.uvc.addWidget(tk.Button(self.TIPO_PAGE.uvc, 
                                text="Atrás", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "1",
                                bd = "3",
                                font = self.TIPO_PAGE.fontStyle3,
                                command = self.main_page), 35, 550)
        
        # Add frame to the window list
        self.frame_list.append(self.MAIN_PAGE)

    def pagina_alumnos(self):
        self.deleteFrames()
        self.ALUMNOS_PAGE = UniViewF(self, "assets\\alumnosbkg.png")
        self.ALUMNOS_PAGE.pack_frame(0,0)

        # Escoger tipo de captura 
        self.opCaptura = "ALUMNO"
        self.opConsulta = "ALUMNO"

        # Matrícula Widgets
        self.ALUMNOS_PAGE.uvc.addWidget(tk.Label(self.ALUMNOS_PAGE.uvc, text="Matrícula:", justify = tk.LEFT), 400, 100)
        self.entryMatri = self.ALUMNOS_PAGE.uvc.addWidget(tk.Entry(self.ALUMNOS_PAGE.uvc, width = 20), 510, 100)

        # Nombre Widgets                
        self.ALUMNOS_PAGE.uvc.addWidget(tk.Label(self.ALUMNOS_PAGE.uvc, text="Nombre:", justify = tk.LEFT), 400, 120)
        self.entryNombre = self.ALUMNOS_PAGE.uvc.addWidget(tk.Entry(self.ALUMNOS_PAGE.uvc, width = 20), 510, 120)
        
        # Carrera Widgets
        self.ALUMNOS_PAGE.uvc.addWidget(tk.Label(self.ALUMNOS_PAGE.uvc, text="Carrera:", justify = tk.LEFT), 400, 140)
        self.entryCarrera = self.ALUMNOS_PAGE.uvc.addWidget(tk.Entry(self.ALUMNOS_PAGE.uvc, width = 20), 510, 140)
        
        # Plan Widgets
        self.ALUMNOS_PAGE.uvc.addWidget(tk.Label(self.ALUMNOS_PAGE.uvc, text="Plan:", justify = tk.LEFT), 400, 160)
        self.entryPlan = self.ALUMNOS_PAGE.uvc.addWidget(tk.Entry(self.ALUMNOS_PAGE.uvc, width = 20), 510, 160)

        # Dirección Widgets
        self.ALUMNOS_PAGE.uvc.addWidget(tk.Label(self.ALUMNOS_PAGE.uvc, text="Dirección:", justify = tk.LEFT), 400, 180)
        self.entryDireccion =  self.ALUMNOS_PAGE.uvc.addWidget(tk.Entry(self.ALUMNOS_PAGE.uvc, width = 20), 510, 180)

        # Teléfono Widgets
        self.ALUMNOS_PAGE.uvc.addWidget(tk.Label(self.ALUMNOS_PAGE.uvc, text="Teléfono:", justify = tk.LEFT), 400, 200)
        self.entryTele = self.ALUMNOS_PAGE.uvc.addWidget(tk.Entry(self.ALUMNOS_PAGE.uvc, width = 20), 510, 200)


        # Capturar Alumnos Button
        self.ALUMNOS_PAGE.uvc.addWidget(tk.Button(self.ALUMNOS_PAGE.uvc, 
                                text="Capturar Datos", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font = self.ALUMNOS_PAGE.fontStyle3,
                                command = self.bCaptuDatosEvent), 200, 250)
        
        # Consulta Datos Button
        self.ALUMNOS_PAGE.uvc.addWidget(tk.Button(self.ALUMNOS_PAGE.uvc, 
                                text="Consultar Datos", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font = self.ALUMNOS_PAGE.fontStyle3,
                                command = self.bConsultaEvent), 400, 250)
        
        # Consulta Matricula Button
        self.ALUMNOS_PAGE.uvc.addWidget(tk.Button(self.ALUMNOS_PAGE.uvc, 
                                text="Consultar Matrícula", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font = self.ALUMNOS_PAGE.fontStyle3,
                                command = self.bConsultaMatEvent), 600, 250)
        
        # Consultar Carrera
        self.ALUMNOS_PAGE.uvc.addWidget(tk.Button(self.ALUMNOS_PAGE.uvc,  
                                text="Consultar Carrera", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font =self.ALUMNOS_PAGE.fontStyle3,
                                command = self.bConsultarCarrEvent), 800, 250)
        
        # NO SCROLLBAR TEXTBOX
        #self.textBox = self.ALUMNOS_PAGE.uvc.addWidget(tk.Text(self.ALUMNOS_PAGE.uvc, width = 80, height = 10), 500, 400)
        
        # SCROLLBAR TEXTBOX
        self.textBox = self.ALUMNOS_PAGE.uvc.addWidget(ts.ScrolledText(self.ALUMNOS_PAGE.uvc, width = 80, height = 10), 500, 400)
                                
        
        # Atrás Button
        self.ALUMNOS_PAGE.uvc.addWidget(tk.Button(self.ALUMNOS_PAGE.uvc,
                                text="Atrás", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "1",
                                bd = "3",
                                font = self.ALUMNOS_PAGE.fontStyle3,
                                command = self.pagina_tipo), 35, 550)
        

        # Add frame to the window list
        self.frame_list.append(self.MAIN_PAGE)

    def bCaptuDatosEvent(self):

        # Enable textBox
        self.textBox.configure(state = tk.NORMAL)
        
        # Get data from Entries
        datos = self.obtenerDatos()
        
        # Delete current textBox content
        self.textBox.delete("1.0",tk.END)

        # Get results from query
        resultado = self.universidad.capturar(datos, self.opCaptura)
        

        # Conditionals depending on query results
        if datos == "VACIO":
            messagebox.showwarning(message="Algún campo está vacio.", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return
        
        if resultado == "Error en la Captura de Datos REVISE LOS CAMPOS..." and datos != "VACIO":
            messagebox.showwarning(message="Error, revise los campos e intente otra vez.", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return

        else:
            # Inserts the result and disables the textBox
            self.textBox.insert(tk.INSERT,resultado)
            self.textBox.configure(state = tk.DISABLED)


    def bConsultaEvent(self):
        self.textBox.configure(state = tk.NORMAL)
        self.textBox.delete("1.0",tk.END)
        datos = self.universidad.consultar(self.opConsulta)

        if datos == "":
            messagebox.showwarning(message="El registro introducido no existe.", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return
            
        self.textBox.insert(tk.INSERT,datos)
        self.textBox.configure(state = tk.DISABLED)
    

    def bConsultarCarrEvent(self):
        self.textBox.configure(state = tk.NORMAL)
        self.textBox.delete("1.0",tk.END)
        
        carr = self.tfCarrera.get()
        datos = self.universidad.consultarCar(carr)

        if carr == "":
            messagebox.showwarning(message="Por favor introduzca una Carrera.", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return


        if (datos == "No se localizo el Alumnos con Carrera "+carr) and (carr != ""):
            messagebox.showwarning(message="La Carrera " + carr + " no pudo ser localizada.", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return

        self.textBox.insert(tk.INSERT,datos)
        self.textBox.configure(state = tk.DISABLED)

    def bConsultaMatEvent(self):
        self.textBox.configure(state = tk.NORMAL)
        self.textBox.delete("1.0",tk.END)
        
        matri = self.tfMatri.get()
        datos = self.universidad.consultarMat(matri)

        if matri == "":
            messagebox.showwarning(message="Por favor introduzca una Matrícula.", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return

        if (datos == "No se localizo la matrícula " + matri) and (matri != ""):
            messagebox.showwarning(message="La Matrícula " + matri + " no pudo ser localizada.", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return
        self.textBox.insert(tk.END,datos)
        self.textBox.configure(state = tk.DISABLED)


    def pagCursa(self):
        self.deleteFrames()
        self.CURSA_PAGE = UniViewF(self, "assets\\cursabkg.png")
        self.CURSA_PAGE.pack_frame(0,0)

        # Escoger tipo de captura
        self.opCaptura = "CURSA"
        self.opConsulta = "CURSA"

        self.lbMatri  = self.CURSA_PAGE.uvc.addWidget(tk.Label(self.CURSA_PAGE.uvc, text="Matrícula:", justify = tk.LEFT), 400, 100)
        self.tfMatri = self.CURSA_PAGE.uvc.addWidget(tk.Entry(self.CURSA_PAGE.uvc, width = 20), 510, 100)
                        
        self.lbClave = self.CURSA_PAGE.uvc.addWidget(tk.Label(self.CURSA_PAGE.uvc, text="Clave:", justify = tk.LEFT), 400, 120)
        self.tfClave = self.CURSA_PAGE.uvc.addWidget(tk.Entry(self.CURSA_PAGE.uvc, width = 20), 510, 120)
        
        self.lbGrupo   = self.CURSA_PAGE.uvc.addWidget(tk.Label(self.CURSA_PAGE.uvc, text="Grupo:", justify = tk.LEFT), 400, 140)
        self.tfGrupo   = self.CURSA_PAGE.uvc.addWidget(tk.Entry(self.CURSA_PAGE.uvc, width = 20), 510, 140)
        
        self.lbSalon = self.CURSA_PAGE.uvc.addWidget(tk.Label(self.CURSA_PAGE.uvc, text="Salon:", justify = tk.LEFT), 400, 160)
        self.tfSalon  = self.CURSA_PAGE.uvc.addWidget(tk.Entry(self.CURSA_PAGE.uvc, width = 20), 510, 160)

        self.lbHorario  = self.CURSA_PAGE.uvc.addWidget(tk.Label(self.CURSA_PAGE.uvc, text="Horario:", justify = tk.LEFT), 400, 180)
        self.tfHorario = self.CURSA_PAGE.uvc.addWidget(tk.Entry(self.CURSA_PAGE.uvc, width = 20), 510, 180)


        self.bCaptuDatosCursa = self.CURSA_PAGE.uvc.addWidget(tk.Button(self.CURSA_PAGE.uvc, 
                                text="Capturar Datos", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font = self.CURSA_PAGE.fontStyle3,
                                command = self.bCaptuDatosEvent), 755, 250)
        
        self.bConsultaCursa = self.CURSA_PAGE.uvc.addWidget(tk.Button(self.CURSA_PAGE.uvc, 
                                text="Consultar Datos", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font = self.CURSA_PAGE.fontStyle3,
                                command = self.bConsultaEvent), 245, 250)

        ## Text Box
            
        self.textBox = self.CURSA_PAGE.uvc.addWidget(ts.ScrolledText(self.CURSA_PAGE.uvc, width = 80, height = 10), 500, 400)
        
        
        ## Boton Atrás
        self.backPagTipo = self.CURSA_PAGE.uvc.addWidget(tk.Button(self.CURSA_PAGE.uvc, 
                                text="Atrás", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "1",
                                bd = "3",
                                font = self.CURSA_PAGE.fontStyle3,
                                command = self.pagina_tipo), 35, 550)
        
        self.frame_list.append(self.MAIN_PAGE)    

    def pagCurso(self):
        self.deleteFrames()
        self.CURSO_PAGE = UniViewF(self, "assets\\cursobkg.png")
        self.CURSO_PAGE.pack_frame(0,0)

        # Escoger tipo de captura
        self.opCaptura = "CURSO"
        self.opConsulta = "CURSO"


        self.lbClave  = self.CURSO_PAGE.uvc.addWidget(tk.Label(self.CURSO_PAGE.uvc, text="Clave:", justify = tk.LEFT), 400, 100)
        self.tfClave = self.CURSO_PAGE.uvc.addWidget(tk.Entry(self.CURSO_PAGE.uvc, width = 20), 510, 100)
                        
        self.lbNombre = self.CURSO_PAGE.uvc.addWidget(tk.Label(self.CURSO_PAGE.uvc, text="Nombre:", justify = tk.LEFT), 400, 120)
        self.tfNombre = self.CURSO_PAGE.uvc.addWidget(tk.Entry(self.CURSO_PAGE.uvc, width = 20), 510, 120)
        
        self.lbSemestre  = self.CURSO_PAGE.uvc.addWidget(tk.Label(self.CURSO_PAGE.uvc, text="Semestre:", justify = tk.LEFT), 400, 140)
        self.tfSemestre   = self.CURSO_PAGE.uvc.addWidget(tk.Entry(self.CURSO_PAGE.uvc, width = 20), 510, 140)


        self.bCaptuDatosCurso = self.CURSO_PAGE.uvc.addWidget(tk.Button(self.CURSO_PAGE.uvc, 
                                text="Capturar Datos", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font = self.CURSO_PAGE.fontStyle3,
                                command = self.bCaptuDatosEvent), 755, 250)
        
        self.bConsultaCurso = self.CURSO_PAGE.uvc.addWidget(tk.Button(self.CURSO_PAGE.uvc, 
                                text="Consultar Datos", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font = self.CURSO_PAGE.fontStyle3,
                                command = self.bConsultaEvent), 500, 250)
        
        self.bConsultaCveCurso = self.CURSO_PAGE.uvc.addWidget(tk.Button(self.CURSO_PAGE.uvc, 
                                text="Consultar Clave", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font = self.CURSO_PAGE.fontStyle3,
                                command = self.bConsultaCveCursoEvent), 245, 250)

        ## Text Box

        self.textBox = self.CURSO_PAGE.uvc.addWidget(ts.ScrolledText(self.CURSO_PAGE.uvc, width = 80, height = 10), 500, 400)
        
        
        ## Boton Atrás
        self.backPagTipo = self.CURSO_PAGE.uvc.addWidget(tk.Button(self.CURSO_PAGE.uvc, 
                                text="Atrás", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "1",
                                bd = "3",
                                font = self.CURSO_PAGE.fontStyle3,
                                command = self.pagina_tipo), 35, 550)
        
        self.frame_list.append(self.MAIN_PAGE)

    def pagReporte(self):
        self.deleteFrames()
        self.REPORTE_PAGE = UniViewF(self, "assets\\reportebkg.png")
        self.REPORTE_PAGE.pack_frame(0,0)

        # Escoger tipo de captura
        self.opConsulta = "TOMAR LISTA"


        self.lbMatri  = self.REPORTE_PAGE.uvc.addWidget(tk.Label(self.REPORTE_PAGE.uvc, text="Matrícula:", justify = tk.LEFT), 400, 100)
        self.tfMatri = self.REPORTE_PAGE.uvc.addWidget(tk.Entry(self.REPORTE_PAGE.uvc, width = 20), 510, 100)
                        
        self.lbCurso = self.REPORTE_PAGE.uvc.addWidget(tk.Label(self.REPORTE_PAGE.uvc, text="Curso:", justify = tk.LEFT), 400, 120)
        self.tfCurso = self.REPORTE_PAGE.uvc.addWidget(tk.Entry(self.REPORTE_PAGE.uvc, width = 20), 510, 120)
        

        self.bConsultarLista = self.REPORTE_PAGE.uvc.addWidget(tk.Button(self.REPORTE_PAGE.uvc, 
                                text="Tomar Lista PC", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font = self.REPORTE_PAGE.fontStyle3,
                                command = self.bConsultarListaEvent), 200, 250)
        
        self.bConsultarListaJ = self.REPORTE_PAGE.uvc.addWidget(tk.Button(self.REPORTE_PAGE.uvc, 
                                text="Tomar Lista JOIN", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font = self.REPORTE_PAGE.fontStyle3,
                                command = self.bConsultarListaJEvent), 400, 250)
        
        self.bConsultarTrayectoria = self.REPORTE_PAGE.uvc.addWidget(tk.Button(self.REPORTE_PAGE.uvc, 
                                text="Trayectoria PC", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font = self.REPORTE_PAGE.fontStyle3,
                                command = self.bConsultaTrayectoriaEvent), 600, 250)

        self.bConsultarTrayectoriaJ = self.REPORTE_PAGE.uvc.addWidget(tk.Button(self.REPORTE_PAGE.uvc, 
                                text="Trayectoria JOIN", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "2",
                                bd = "3",
                                font = self.REPORTE_PAGE.fontStyle3,
                                command = self.bConsultaTrayectoriaJEvent), 800, 250)

        ## Text Box

        self.textBox = self.REPORTE_PAGE.uvc.addWidget(ts.ScrolledText(self.REPORTE_PAGE.uvc, width = 80, height = 10), 500, 400)
        
        
        ## Boton Atrás
        self.backPagTipo = self.REPORTE_PAGE.uvc.addWidget(tk.Button(self.REPORTE_PAGE.uvc, 
                                text="Atrás", 
                                anchor = tk.CENTER,
                                bg = "#A31F34",
                                foreground = "white",
                                width = "18",
                                height = "1",
                                bd = "3",
                                font = self.REPORTE_PAGE.fontStyle3,
                                command = self.pagina_tipo), 35, 550)
        
        self.frame_list.append(self.MAIN_PAGE)

    def bConsultaTrayectoriaEvent(self):
        self.textBox.configure(state = tk.NORMAL)
        self.textBox.delete("1.0",tk.END)
        
        matri = self.tfMatri.get()
        datos = self.universidad.consultarTrayectoria(matri, 0)

        if matri == "":
            messagebox.showwarning(message="Por favor introduzca una Matrícula.", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return

        if (datos == "") and (matri != ""):
            messagebox.showwarning(message="La Matrícula " + matri + " no pudo ser localizada.", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return
        self.textBox.insert(tk.INSERT,datos)
        self.textBox.configure(state = tk.DISABLED)


    def bConsultaTrayectoriaJEvent(self):

        self.textBox.configure(state = tk.NORMAL)

        self.textBox.delete("1.0",tk.END)
        
        matri = self.tfMatri.get()
        datos = self.universidad.consultarTrayectoria(matri, 1)

        if matri == "":
            messagebox.showwarning(message="Por favor introduzca una Matrícula.", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return

        if (datos == "") and (matri != ""):
            messagebox.showwarning(message="La Matrícula " + matri + " no pudo ser localizada.", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return
        self.textBox.insert(tk.INSERT,datos)
        self.textBox.configure(state = tk.DISABLED)


    def bConsultarListaEvent(self):
        self.textBox.configure(state = tk.NORMAL)
        self.textBox.delete("1.0",tk.END)
        
        curso = self.tfCurso.get()
        datos = self.universidad.consultarLista(curso, 0)

        if curso == "":
            messagebox.showwarning(message="Por favor introduzca una Curso.", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return


        if (datos == "") and (curso != ""):
            messagebox.showwarning(message="No hay alumnos inscritos en " + curso + ".", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return
        self.textBox.insert(tk.INSERT,datos)
        self.textBox.configure(state = tk.DISABLED)

    
    def bConsultarListaJEvent(self):
        self.textBox.configure(state = tk.NORMAL)
        self.textBox.delete("1.0",tk.END)
        
        curso = self.tfCurso.get()
        datos = self.universidad.consultarLista(curso, 1)

        if curso == "":
            messagebox.showwarning(message="Por favor introduzca una Curso.", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return


        if (datos == "") and (curso != ""):
            messagebox.showwarning(message="No hay alumnos inscritos en " + curso + ".", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return

        self.textBox.insert(tk.INSERT,datos)
        self.textBox.configure(state = tk.DISABLED)


    def bConsultaCveCursoEvent(self):
        self.textBox.configure(state = tk.NORMAL)
        self.textBox.delete("1.0",tk.END)
        
        cveCurso = self.tfClave.get()
        datos = self.universidad.consultarCveCurso(cveCurso)

        if cveCurso == "":
            messagebox.showwarning(message="Introduzca una clave de curso.", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return

        if (datos == "No se localizo el curso con esa clave "+cveCurso) and (cveCurso != ""):
            messagebox.showwarning(message="El Curso con Clave " + cveCurso + " no pudo ser localizado.", title="MIT DataBase Manager")
            self.textBox.configure(state = tk.DISABLED)
            return
        
        self.textBox.insert(tk.INSERT,datos)
        self.textBox.configure(state = tk.DISABLED)


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


    def start_GUI(self):
        self.mainloop()


    def on_closing(self):
        if messagebox.askokcancel(message="¿Está seguro que quiera salir?", title="MIT DataBase Manager"):
            self.destroy()


    def obtenerDatos(self):
        matri  = ""
        nom  = ""
        car = ""
        plan = ""
        dire = ""
        tel = ""
        clav = ""
        grupo = ""
        sal = ""
        hora = ""
        clav = ""
        cnom = ""
        sem = ""

        if self.opCaptura == "ALUMNO":
            matri  = self.entryMatri.get()
            matri = str.upper(matri)
            nom  = self.entryNombre.get()
            nom = str.upper(nom)
            car = self.entryCarrera.get()
            car = str.upper(car)
            plan = self.entryPlan.get()
            plan = str.upper(plan)
            dire = self.entryDireccion.get()
            dire = str.upper(dire)
            tel = self.entryTele.get()
            tel = str.upper(tel)

            datos = matri + "_" + nom + "_" + car + "_" + plan + "_" + dire + "_" + tel
        
        if self.opCaptura == "CURSA":
            matri  = self.tfMatri.get()
            matri = str.upper(matri)
            clav = self.tfClave.get()
            clav = str.upper(clav)
            grupo = self.tfGrupo.get()
            grupo = str.upper(grupo)
            sal = self.tfSalon.get()
            sal = str.upper(sal)
            hora = self.tfHorario.get()
            hora = str.upper(hora)
            
            datos = matri + "_" + clav + "_" + grupo + "_" + sal + "_" + hora 
        
        if self.opCaptura == "CURSO":
            clav = self.tfClave.get()
            clav = str.upper(clav)
            cnom = self.tfNombre.get()
            cnom = str.upper(cnom)
            sem = self.tfSemestre.get()
            sem = str.upper(sem)
            datos = clav + "_" + cnom + "_" + sem

        if ((matri == "" or nom == "" or car == "" or plan == "" or dire == "" or tel == "") and (matri == "" or clav == "" or grupo == "" or hora == "" or sal == "")
            and (clav == "" or cnom == "" or sem == "")):
            datos = "VACIO"
        return datos

    def deleteFrames(self):
        for frame in self.frame_list:
            frame.destroy()
            self.frame_list.remove(frame)

class UniViewF(tk.Frame):
    def __init__(self, ROOT, BKG_PATH):
            # Atributos CONSTANTES
            self.BKG_PATH = BKG_PATH
            self.BORDER_WIDTH=0
            self.HIGHLIGHT_THICKNESS=0
            self.WIDTH = 1000
            self.HEIGHT = 600
            self.HIGHLIGHT_COLOR = '#E4E4E4'
            self.BG = "#E4E4E4"
            

            # FRAME constructor
            super().__init__(ROOT, borderwidth = self.BORDER_WIDTH, highlightthickness = self.HIGHLIGHT_THICKNESS, 
                            highlightbackground = self.HIGHLIGHT_COLOR, width = self.WIDTH, height = self.HEIGHT, bg = self.BG)
            self.uvc = UniViewC(self, BKG_PATH)

            # FONST
            self.fontStyle = tkFont.Font(family="Montserrat ExtraBold", size=30)
            self.fontStyle2 = tkFont.Font(family="Montserrat ExtraBold", size=12)
            self.fontStyle3 = tkFont.Font(family="Montserrat ExtraBold", size=9)

    def pack_frame(self, COLUMN, ROW):
            self.grid(column = COLUMN, row = ROW)
    
    
    def delete_frame(self):
            self.destroy()

class UniViewC(tk.Canvas):
    def __init__(self, FRAME, BKG_PATH):
        # Atributos CONSTANTES
        self.BORDER_WIDTH=0
        self.HIGHLIGHT_THICKNESS=0
        self.HIGHLIGHT_COLOR = '#E4E4E4'
        self.WIDTH = 1000
        self.HEIGHT = 600
        
        # Atributos VARIABLES
        self.BKG_PATH = os.path.abspath(BKG_PATH)


        # CANVAS constructor!
        super().__init__(FRAME, width = self.WIDTH, height = self.HEIGHT, 
                        highlightthickness = self.HIGHLIGHT_THICKNESS, highlightbackground = self.HIGHLIGHT_COLOR)

        # BKG setup!
        # BUG MYSTERIOUS PADDING WHEN THICKNESS != 0 CHECK TEMP

        self.pil_img = Image.open(self.BKG_PATH)
        self.r_img = self.pil_img.resize((self.WIDTH, self.HEIGHT))
        self.img = ImageTk.PhotoImage(self.r_img)
        self.bg = self.create_image(0, 0, anchor = tk.NW, image=self.img)
        
        
        # CANVAS Geometry Manager
        self.place(x = 0, y = 0)
    
    def addWidget(self, widget, x, y):
        self.create_window(x, y, anchor=tk.CENTER, window=widget)
        return widget
