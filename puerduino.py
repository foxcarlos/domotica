import serial
import time
from pygame import mixer

mixer.init()
mixer.music.load('/home/cgarcia/desarrollo/python/pyganzo/campana.mp3')

def main():
    while 1:
        s = serial.Serial("/dev/ttyACM1")
        recv = s.readline()
        if 'Movimiento' in recv:
            print recv.split()
            #mixer.music.play()
            #time.sleep(2)
        else:
            print recv.split()

if __name__ == '__main__':
    main()
