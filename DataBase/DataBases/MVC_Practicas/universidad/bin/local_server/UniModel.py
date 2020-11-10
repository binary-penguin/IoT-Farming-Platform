#!/usr/bin/python
# _*_ coding: utf-8 _*_

import mysql.connector      # NON-STANDARD
    
import subprocess           # STANDARD
import time # STANDARD
import os # STANDARD

# M-O-D-E-L   
# Manages all data logic
# Executes queries
# Administrates Files

''' Model Object of Universidad'''

class UniModel:
    command__ = ''
    query__ = ''
    response_ = []
    HOST__ = ''
    PORT__ = ''
    USER__ = ''
    PASSWORD__ = ''
    DATABASE__ = ''

    def __init__(self, host_, port_, user_, password_, database_):


        # Retrieves user credentials!
        self.HOST__ = host_
        self.PORT__ = port_
        self.USER__ = user_
        self.PASSWORD__ = password_
        self.DATABASE__ = database_

        os.system("clear")
        print()
        print("WELCOME TO MIT DATABASE MANAGER \U0001F4DA")
        print()

    def runServer(self):
        self.runSubprocess("mysqld --explicit_defaults_for_timestamp")

    def accessDB(self):
            self.cnx__ = mysql.connector.connect(host = self.HOST__, port = self.PORT__, user = self.USER__, 
                                                password = self.PASSWORD__, database = self.DATABASE__)
    
    def closeApp(self):
        print()
        
        

    def pause(self):
        print("[ENTER] para continuar.")
    
    def successConsole(self, message):
        print("\u2714\ufe0f........." + message)
        time.sleep(1)
    
    def errorConsole(self, message):
        print("\u274C........." + message)
        time.sleep(1)
    def runSubprocess(self, command):
        subprocess.Popen(command)