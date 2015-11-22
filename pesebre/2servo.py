import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT)

pwm = GPIO.PWM(21, 50)
pwm.start(7.5)

try:
    while True:
	pwm.ChangeDutyCycle(12)
	time.sleep(1)
	pwm.ChangeDutyCycle(4.5)
	time.sleep(1)
	#pwm.ChangeDutyCycle(4.5)
	#time.sleep(1)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()



