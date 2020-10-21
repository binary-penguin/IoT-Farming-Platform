import tkinter as tk  # Package de Python 3.7
from tkinter import messagebox # Package para desplegar ventanas
import tkinter.font as tkFont # Package para personalizar tipografías
from PIL import Image, ImageTk # Package que permite el manejo de distintos formatos de imagen


class WindowCreator(tk.Frame):
    def __init__(self, parent, file_path, width, height):
        
        super(WindowCreator, self).__init__(parent, borderwidth=0, highlightthickness=0, width = 1000, height = 600)    
        self.fontStyle = tkFont.Font(family="Montserrat ExtraBold", size=30)
        self.fontStyle2 = tkFont.Font(family="Montserrat ExtraBold", size=12)
        self.canvas = tk.Canvas(self, width=width, height=height)
        
        self.pil_img = Image.open(file_path)
        self.img = ImageTk.PhotoImage(self.pil_img.resize((width, height), Image.ANTIALIAS))
        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        self.canvas.pack()

        
    def changeBkg(self, file_path, width, height):
        self.pil_img = Image.open(file_path)
        self.img = ImageTk.PhotoImage(self.pil_img.resize((width, height), Image.ANTIALIAS))
        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

    def add(self, widget, x, y):
        self.canvas.create_window(x, y, anchor=tk.CENTER, window=widget)
        return widget
    
    def addTextScroll(self, widget):

        self.canvas.create_window(anchor=tk.CENTER, window=widget)
        return widget


        
    


