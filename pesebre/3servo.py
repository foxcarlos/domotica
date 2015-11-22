import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

pwm1 = GPIO.PWM(23, 50)
pwm2 = GPIO.PWM(21, 50)

pwm1.start(12)
pwm2.start(1)

try:
    while True:
	
        pwm1.ChangeDutyCycle(4.5)
	time.sleep(1)

	pwm2.ChangeDutyCycle(12)
	time.sleep(1)

	pwm1.ChangeDutyCycle(12)
	time.sleep(1)

	#pwm2.ChangeDutyCycle(12)
	time.sleep(5)

except KeyboardInterrupt:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()



