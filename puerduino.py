import serial
import time

def main():
    while 1:
        s = serial.Serial("/dev/ttyACM1")
        recv = s.readline()
        print recv.split()
        time.sleep(2)

if __name__ == '__main__':
    main()
