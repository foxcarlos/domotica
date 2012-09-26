#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Dispositivo Arduino conectado a un circuito Electronico que
permite abrir una cerradura electrica o hembrilla Electrica

Script de practicas que permite ejecutar un server socket
que esta a la espera de un envio via socket (via android para mi caso)
de la contraseña, si la contraseña esta en la lista claves[]
este enviara via puerto serial un pulso al dispositivo Arduino 
con el cual se abrira la cerradura Electrica o hembrilla Electrica
'''

import socket
import time
import serial


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 8000))
server.listen(1)

s = serial.Serial("/dev/ttyACM0")

claves = ['11951', 'carlos']

while 1:
    print "Esperando clientes..."
    socket_cliente, datos_cliente = server.accept()
    print "conectado cliente:" + str(datos_cliente)
    seguir = True
    while seguir:
        peticion = socket_cliente.recv(1024)
        if peticion in claves:
            s.write('1')
        else:
            s.write('0')
        
        time.sleep(3)
        socket_cliente.close()
        break

server.close()
