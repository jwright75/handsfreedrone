import serial
from pyautogui import press

ser = serial.Serial('COM3', baudrate = 115200, timeout=0)

while 0:

	arduinoX = ser.readline()
	arduinoY = ser.readline()
	arduinoZ = ser.readline()
	if int(arduinoX) > 8200 :
		press('f')
	else:
		press('b')

	if int(arduinoY) > 8200 :
		press('d')
	else:
		press('u')

	if int(arduinoZ) > 8200 :
		press('r')
	else:
		press('l')
		
	