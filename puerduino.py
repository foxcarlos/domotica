import serial

def main():
    while 1:
        s = serial.Serial("/dev/ttyACM0")
        recv = s.readline()
        print recv.split()

if __name__ == '__main__':
    main()
