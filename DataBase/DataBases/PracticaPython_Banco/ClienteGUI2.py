#from Tkinter import *   # Package de Python 2.7
from tkinter import *    # Package de Python 3.7

#from BancoAD import BancoAD
from BancoADjdbc import BancoADjdbc

class ClienteGUI2:
    frame = Tk()
    
    #banco = BancoAD()
    banco = BancoADjdbc()
    
    # Constructor
    def __init__(self):
        # 1. Definicion y creacion del objeto frame (Tk) (JFrame)
        #self.frame = Tk()
        self.frame.title("Bancomer: Gestion de Clientes")
        self.frame.geometry("600x400")

        # 2. Definicion y creacion de los atributos del frame
        self.lbClave  = Label(self.frame, text="NO. DE CUENTA:")
        self.tfClave  = Entry(self.frame, width=20) # Entry 
        
        self.lbNombre = Label(self.frame, text="NOMBRE:")
        self.tfNombre = Entry(self.frame, width=20)
        
        self.lbTipo   = Label(self.frame, text="TIPO DE CUENTA:")
        self.tfTipo   = Entry(self.frame, width=20);
        
        self.lbSaldo  = Label(self.frame, text="SALDO:")
        self.tfSaldo  = Entry(self.frame, width=20)
        
        self.bCapturar    = Button(self.frame, text="Capturar Datos", command=self.bCapturarEvent)
        self.bConsultar   = Button(self.frame, text="Consultar Datos",command=self.bConsultarEvent)
        self.bConsultarTC = Button(self.frame, text="Consultar Tipo Cuenta",command=self.bConsultarTCEvent)
        self.bConsultarNC = Button(self.frame, text="Consultar No. Cuenta",command=self.bConsultarNCEvent)
   
        self.taDatos      = Text(self.frame, width=40, height=10)        
        
        # 3. Colocar los objetos de los atributos en un Layout
        self.lbClave.grid(row=0, column=0)
        self.tfClave.grid(row=0, column=1)
        
        self.lbNombre.grid(row=1, column=0)
        self.tfNombre.grid(row=1, column=1)
        
        self.lbTipo.grid(row=2, column=0)
        self.tfTipo.grid(row=2, column=1)
        
        self.lbSaldo.grid(row=3, column=0)
        self.tfSaldo.grid(row=3, column=1)
        
        self.bCapturar.grid(row=4, column=0)
        self.bConsultar.grid(row=4, column=1)
        self.bConsultarTC.grid(row=5, column=0)
        self.bConsultarNC.grid(row=5, column=1)
        self.taDatos.grid(row=7, column=0)

        # Hacer visible al frame
        self.frame.mainloop()
    
    # Metodos de la class ClienteGUI
    def obtenerDatos(self):
        cve  = self.tfClave.get()
        nom  = self.tfNombre.get()
        tipo = self.tfTipo.get()
        saldo = self.tfSaldo.get()
        
        if cve == "" or nom == "" or tipo == "" or saldo == "":
            datos = "VACIO"
        else:
            try:
                valor = float(saldo)
                #datos = cve+'_'+nom+'_'+tipo+'_'+saldo # Concatenacion correcta
                datos = cve+"_"+nom+"_"+tipo+"_"+saldo  # Concatenacion correcta
            except:
                datos = "NO_NUMERICO"
        
        return datos
    
    def bCapturarEvent(self):
        datos = self.obtenerDatos()
        
        self.taDatos.delete("1.0",END)
        
        if datos == "VACIO":
            self.taDatos.insert(END,"Algun campo esta vacio...")
        else:
            if datos == "NO_NUMERICO":
                self.taDatos.insert(END,"Saldo debe ser numerico...")
            else:
                resultado = self.banco.capturar(datos)
                self.taDatos.insert(END,resultado)
    
    def bConsultarEvent(self):
        self.taDatos.delete("1.0",END)
        
        datos = self.banco.consultar()
        self.taDatos.insert(END,datos)
    
    def bConsultarNCEvent(self):
        self.taDatos.delete("1.0",END)
        
        ncta = self.tfClave.get()
        datos = self.banco.consultarCta(ncta)
        self.taDatos.insert(END,datos)

    def bConsultarTCEvent(self):
        self.taDatos.delete("1.0",END)
        
        tipo = self.tfTipo.get()
        datos = self.banco.consultarTipo(tipo)
        self.taDatos.insert(END,datos)

# CREACCION DEL OBJETO cliente de la class ClienteGUI (main() de C y Java)
cliente = ClienteGUI2()


