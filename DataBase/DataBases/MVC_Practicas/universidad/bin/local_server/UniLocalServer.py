#!/usr/bin/python
# _*_ coding: utf-8 _*_

import socket
from BancoADjdbc import BancoADjdbc


class UniLocalServer(socket.socket):

    # Constructor
    def __init__(self):
        self.cont = BancoADjdbc()
        # Iniciar el Seerver con als funciones establecidas por el API Sockets
        self.server = super(socket.AF_INET, socket.SOCK_STREAM)
        self.connection_socket = super(socket.AF_INET, socket.SOCK_STREAM)


        # TODO MAKE THE 2D ARRAYS TO HANDLE TRAFFIC    
        self.request_list = []
        self.client_list = []
        self.connection_list = []
        

    def setup(self):
        # IP ADRESS + PORT
        # (LOCAL IP) OR (ROUTER IP)
        self.server.bind(("192.168.100.220",777))
        self.server.listen(5)
        print("Socket was opened...")
    
    def run(self):

        # Infinite loop

        while True:
            print("Listening for connections ...")

            connection_socket, client = self.server.accept()
            self.client_list.append(client)
            self.connection_list.append(connection_socket)

            print("Connection to " + str(client) + " was made with success!")
            
            # Checks requests and decodes it
            request = connection_socket.recv(1024).decode()
            self.request_list.append(request)
            print("Request: " + request)
