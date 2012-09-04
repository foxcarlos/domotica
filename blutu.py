#!/usr/bin/env python

import bluetooth
import os

salir = False
mi_telefono = 'AC:E8:7B:6E:51:9C'

while not salir:
    encontrados = bluetooth.discover_devices(duration=4, flush_cache=True, lookup_names=False)
    if mi_telefono in encontrados:
        print 'Desbloquear'
        os.system('gnome-screensaver-command -d')
    else:
        print 'Bloquear'
        os.system('gnome-screensaver-command -l')




