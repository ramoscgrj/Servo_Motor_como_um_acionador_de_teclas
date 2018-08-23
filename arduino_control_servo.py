# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 12:39:44 2018

@author: dti
"""

#import RPi.GPIO as gpio
import time
import serial

arduino=serial.Serial('Port_#0001.Hub_#0004',9600) #comtem erro de atributo no windows

for i in range(5):
    arduino.write(b'0')
    time.sleep(5)
    arduino.write(b'1')
    time.sleep(5)
