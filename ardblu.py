#!/usr/bin/env python

import bluetooth
import os
import serial

salir = False
mi_telefono = 'AC:E8:7B:6E:51:9C'
s = serial.Serial("/dev/ttyACM1")

while not salir:
    encontrados = bluetooth.discover_devices(duration=3, flush_cache=True, lookup_names=False)
    if mi_telefono in encontrados:
        print '1 Abrir Hembrilla'
        #os.system('gnome-screensaver-command -d')
        s.write('1')
    else:
        print '0 No Abrir nada'
        #os.system('gnome-screensaver-command -l')
        s.write('0')
