#!/usr/bin/env python

import serial

salir = False
s = serial.Serial("/dev/ttyACM1")
clave = ['11951', '10101']

while not salir:
    valor = raw_input('Ingrese su codigo:')   
    if valor in clave:
        print '1 Bienvenido'
        s.write('1')
    else:
        print '0 Acceso Denegado'
        s.write('0')
