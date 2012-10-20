#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Script para un telefono Android corriendo mediante SL4A
que permite enviar via socket una contraseña que de ser
la correcta le indica al server socket que debe abrir
la cerradura Electrica o hembrilla Electrica
'''

import socket
import android

if __name__ == '__main__':
   droid = android.Android()
   valor = droid.dialogGetPassword()[1]
   if valor != 'None' or valor !='':
       server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       server.connect(('192.168.1.106', 8000))   
       server.send(str(valor))
