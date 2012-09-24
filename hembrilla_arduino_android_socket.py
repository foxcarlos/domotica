#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import android

if __name__ == '__main__':
   droid = android.Android()
   valor = droid.dialogGetPassword()[1]
   if valor != 'None' or valor !='':
       server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       server.connect(('10.121.3.41', 8000))   
       server.send(str(valor))
