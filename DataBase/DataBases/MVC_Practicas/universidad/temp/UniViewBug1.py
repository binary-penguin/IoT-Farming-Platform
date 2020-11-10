#!/usr/bin/python
# _*_ coding: utf-8 _*_

import tkinter as tk # STANDARD
from tkinter import messagebox # STANDARD
import tkinter.font as tkFont # STANDARD
import tkinter.scrolledtext as ts # STANDARD
from PIL import Image, ImageTk # NON-STANDARD Allows the use of different image formats
import os # STANDARD

# V-I-E-W
# Dynamically renders the GUI


# 1. ROOT -> 2. FRAME -> 3. CANVAS

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

            self.uvf = UniViewF(self)

            #self.root.grid(row = 0, column = 0)
    def startGUI(self):
        self.mainloop()     
        
    
    def on_closing(self):
        if messagebox.askokcancel(message="¿Está seguro que quiera salir?", title="MIT DataBase Manager"):
            self.destroy()


class UniViewF(tk.Frame):
    def __init__(self, ROOT):
            print("DENTRO DE FRAME")
            # Atributos CONSTANTES
            self.BORDER_WIDTH=0
            self.HIGHLIGHT_THICKNESS=0
            self.WIDTH = 700
            self.HEIGHT = 500
            self.HIGHLIGHT_COLOR = 'white'
            self.BG = "blue"
            # Atributos VARIABLES
            self.fontStyle = tkFont.Font(family="Montserrat ExtraBold", size=30)
            self.fontStyle2 = tkFont.Font(family="Montserrat ExtraBold", size=12)
            self.fontStyle3 = tkFont.Font(family="Montserrat ExtraBold", size=9)
            self.fontStyle4 = tkFont.Font(family="Montserrat", size=9)

            # FRAME constructor
            super().__init__(ROOT, borderwidth = self.BORDER_WIDTH, highlightthickness = self.HIGHLIGHT_THICKNESS, 
                            highlightbackground = self.HIGHLIGHT_COLOR, width = self.WIDTH, height = self.HEIGHT, bg = self.BG)
            
            self.uvc = UniViewC(self)
            self.grid(column = 0, row = 0)

class UniViewC(tk.Canvas):
    def __init__(self, FRAME):
        print("DENTRO DE CANVAS")
        # Atributos CONSTANTES
        self.BORDER_WIDTH=0
        self.HIGHLIGHT_THICKNESS=0
        self.HIGHLIGHT_COLOR = 'green'
        self.WIDTH = 500
        self.HEIGHT = 300
        
        # Atributos VARIABLES
        self.BKG_PATH = os.path.abspath("assets\\mitbkg.png")


        # CANVAS constructor!
        super().__init__(FRAME, width = self.WIDTH, height = self.HEIGHT, 
                        highlightthickness = self.HIGHLIGHT_THICKNESS, highlightbackground = self.HIGHLIGHT_COLOR)

        # BKG setup!
        # BUG MYSTERIOUS PADDING WHEN THICKNESS != 0

        self.pil_img = Image.open(self.BKG_PATH)
        self.r_img = self.pil_img.resize((self.WIDTH, self.HEIGHT))
        self.img = ImageTk.PhotoImage(self.r_img)
        self.bg = self.create_image(0, 0, anchor = tk.NW, image=self.img)
        
        
        # CANVAS Geometry Manager
        self.place(x = 100, y = 100)