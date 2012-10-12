#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from pygame import mixer
import time

#

'''GPIO.setwarnings(False)  # Deshabilita los warings del GPIO'''

def main():
    mixer.init()
    mixer.music.load('/home/pi/desarrollo/python/domotica/campana3.mp3')
    
    '''Se limpian todos los Pines y se configuran 
    los pines como aparecen en la tarjeta del 1 al 26'''
    
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    
    ''' Se declaran los pines:
        11 como entrada 
        12 como salida
    '''
    GPIO.setup(11, GPIO.IN)
    GPIO.setup(12, GPIO.OUT)
    
    ''' Se declara la variable como falsa ya que solo se 
    enviara un twitt una sola vez por cada vez que se 
    detecta un movimiento, el sensor esta configurado
    para que envie una se;al continua por 3 minutos
    si no se utiliza esta variable se enviaran varios twitts
    mientras se cumplan esos minutos'''
    msg_enviado = False

    while True:
        ''' Se asigna a la Variale ValorRecibido el valor de entrada 
            por el Pin 11 en caso de que lo tenga
        ''' 
        ValorRecibido = GPIO.input(11)
        if ValorRecibido:
            ''' Si se recibio el valor, se encidende el Led
            ubicado en el Pin 12 y se espera 2 segundos para
            apagarlo
            '''
            print('Movimiento detectado...')
            GPIO.output(12, True)
            #mixer.music.play()
            #time.sleep(3)
            
            if not msg_enviado:
                print('Enviar un Twitter.. aunque por ahora solo se emitira un sonido')
                mixer.music.play()
                msg_enviado = True
            

        else:
            GPIO.output(12, False)
            print('Apagando Led...')
            msg_enviado = False

if __name__ == '__main__':
     main()
