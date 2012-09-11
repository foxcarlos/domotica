#!/usr/bin/env python

import bluetooth
import os
import serial

salir = False
mi_telefono = 'AC:E8:7B:6E:51:9C'
s = serial.Serial("/dev/ttyACM0")

while not salir:
    encontrados = bluetooth.discover_devices(duration=4, flush_cache=True, lookup_names=False)
    if mi_telefono in encontrados:
        print '0 Desbloquear'
        #os.system('gnome-screensaver-command -d')
        s.write('0')
    else:
        print '1 Bloquear'
        #os.system('gnome-screensaver-command -l')
        s.write('1')
