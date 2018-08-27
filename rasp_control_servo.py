# -*- coding: utf-8 -*-

import time
import serial

arduino=serial.Serial('/dev/ttyACM0',9600) #comtem erro de atributo no windows
'''
for i in range(3):
    arduino.write(b'0')
    time.sleep(3)
    arduino.write(b'1')
    time.sleep(3)
'''
try:
    request=1
    time.sleep(1)
    while(True):
        time.sleep(1)
        if request==0:
            print(" ")
            print("Equipamento Desligado!")
            time.sleep(1)
            request=int(input("Digite 1 para Ligar: "))
            time.sleep(1)
            arduino.write(b'0')
            time.sleep(1)
        elif request==1:
            print(" ")
            print("Equipamento Ligado!")
            time.sleep(1)
            request=int(input("Digite 0 para Desligar: "))
            time.sleep(1)
            arduino.write(b'1')
            time.sleep(1)
        else:
            print('Fim')
            break
            
except:
    print('Fim')
