import RPi.GPIO as GPIO
import time
import os

pinLed1 = 11
pinLed2 = 13
pinLed3 = 15

pinServoNino = 21
pinServoCortina = 23

cortinaAbajo = 3
cortinaCentro = 5

ocultarNino = 1
mostrarNino = 12

pausa = 2
pausaMostrar = 20

musica = '/home/pi/desarrollo/python/domotica/pesebre/mixnavidad.mp3'


GPIO.setmode(GPIO.BOARD)

GPIO.setup(pinLed1, GPIO.OUT)
GPIO.setup(pinLed2, GPIO.OUT)
GPIO.setup(pinLed3, GPIO.OUT)

GPIO.setup(pinServoNino, GPIO.OUT)
GPIO.setup(pinServoCortina, GPIO.OUT)

nino = GPIO.PWM(pinServoNino, 50)
cortina = GPIO.PWM(pinServoCortina, 50)

# Apagar Leds
GPIO.output(pinLed1, GPIO.LOW)
GPIO.output(pinLed2, GPIO.LOW)
GPIO.output(pinLed3, GPIO.LOW)

print('Preparando Servos')

nino.start(ocultarNino)
cortina.start(cortinaAbajo)
time.sleep(pausa)


try:
    while True:
	print('Inciando...')
	print('centrar cortina')

	cortina.ChangeDutyCycle(cortinaCentro)
	time.sleep(pausa)

	print('Acomodar nino')
	nino.ChangeDutyCycle(mostrarNino)
	time.sleep(pausa)
	
	GPIO.output(pinLed1, GPIO.HIGH)
	print('bajar cortina')
	cortina.ChangeDutyCycle(cortinaAbajo)

	os.system('mpg123 -q {0}&'.format(musica))

	print('espera 20 segundos para motrar al nino jesus')
	time.sleep(pausaMostrar)

	# Apagar Leds
	GPIO.output(pinLed1, GPIO.LOW)
	GPIO.output(pinLed2, GPIO.LOW)
	GPIO.output(pinLed3, GPIO.LOW)

	print('bajar cortina despues de los 20 seg')
	cortina.ChangeDutyCycle(cortinaCentro)
	time.sleep(pausa)

	print('regresar hacia atras al nino')
	nino.ChangeDutyCycle(ocultarNino)
	time.sleep(pausa)

	os.system('killall -v mpg123')

	cortina.ChangeDutyCycle(cortinaAbajo)
	time.sleep(pausaMostrar)

except KeyboardInterrupt:
    nino.start(ocultartNino)
    cortina.start(cortinaAbajo)

    cortina.stop()
    nino.stop()
    
    # Apagar Leds
    GPIO.output(pinLed1, GPIO.LOW)
    GPIO.output(pinLed2, GPIO.LOW)
    GPIO.output(pinLed3, GPIO.LOW)

    GPIO.cleanup()
