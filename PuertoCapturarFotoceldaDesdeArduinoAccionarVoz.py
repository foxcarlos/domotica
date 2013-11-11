import serial
import time
import os 

def main():
    while 1:
        s = serial.Serial("/dev/ttyACM0")
        recv = ''
        try:
            recv = s.read()
            print(recv.strip())
        except:
            print('Error al momento de leer puerto')
        
        if '0' in recv.strip():
            comando_de_voz = "espeak -s140 -v 'es-la'+f2 '%s'" % ('Luz Apagada')
            os.system(comando_de_voz)
            print('Luz Apagada')
            #time.sleep(2)
        elif '1' in recv.strip():
            comando_de_voz = "espeak -s140 -v 'es-la'+f2 '%s'" % ('Luz Encendida')
            os.system(comando_de_voz)
            print('Luz Encendida')
            
if __name__ == '__main__':
    main()
