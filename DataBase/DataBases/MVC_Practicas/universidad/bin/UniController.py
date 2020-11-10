#!/usr/bin/python
# _*_ coding: utf-8 _*_


from UniModel import UniModel # Importing a Class from a file
from UniView import UniViewR   # Importing a Class from a file
import tkinter as tk # STANDARD
import mysql.connector
from mysql.connector import errorcode # NON STANDARD EXCEPTIONS HANDLING    

# C-O-N-T-R-O-L-L-E-R
# Gets userInput to model
# Receives model data
# Passes data to view

''' Controller Object of Universidad'''

class UniController:
    HOST__ = ''
    PORT__ = ''
    USER__ = ''
    PASSWORD__ = ''
    DATABASE__ = ''

    # Duda a resolver, pueden ser objetos atributos de otros objetos, no implica un gasto de memoria ya que se 
    # crean dinamicamente cuando se llaman
    # Objects are not declared, they are not attributes
    # None solo puede asignarse a un objeto
    
    def __init__(self):
        # Defines user credentials!
        self.HOST__ = 'localhost'
        self.PORT__ = '3306'
        self.USER__ = 'root'
        self.PASSWORD__ = ''
        self.DATABASE__ = 'universidad'

        
        # Starts the program!
        try:
            self.um = UniModel(host_ = self.HOST__, port_ = self.PORT__, user_ = self.USER__, 
                            password_ = self.PASSWORD__, database_ = self.DATABASE__)
            self.um.successConsole("Program started successfully!")
        except (OSError, ValueError):
            self.um.errorConsole("Program cannot be started!")
        
        # Runs the server!
        try:
            self.um.runServer()
            self.um.successConsole("Server started successfully!")
        except (OSError, ValueError):
            self.um.errorConsole("Server cannot be started!")      

        # Connects to the DB!
        try:
            self.um.accessDB()
            self.um.successConsole("Connected to the database successfully!")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.um.errorConsole("Something is wrong with your username or password!")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.um.errorConsole("The selected database does not exist!")
        
        # Starts GUI!
        try:
            self.uv = UniViewR()
            self.um.successConsole("GUI started successfully!")
            self.uv.start_GUI()
        except tk.TclError:
            self.um.errorConsole("GUI cannot be started!")
    
    def endProgram(self):
        self.um.runSubprocess("mysqladmin -u root shutdown")
        self.um.successConsole("Cierre de DataBase exitosa.")


if __name__ == "__main__":
    session = UniController()


