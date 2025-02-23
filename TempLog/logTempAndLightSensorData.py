#Reading from /sys/bus/w1/devices/28-3fa9d445207e/w1_slave

import os
import glob
import time
import datetime
import serial

device_file = '/sys/bus/w1/devices/28-3fa9d445207e/w1_slave' 

date = str(datetime.datetime.today().strftime("%Y %m %d"))

with open(device_file, 'r') as f, open(date+'.csv', 'w') as outputfile, serial.Serial('/dev/ttyUSB0', 9600, timeout = 2) as ser:
	while True:
		lines = f.readlines()
		lightval = ser.readline().decode('utf-8')
		ser.reset_input_buffer()
		f.seek(0)
		time.sleep(1)
		try:
			equals_pos = lines[1].find('t=')
		except IndexError:
			print("I",end=' ')
			continue
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			temp_c = float(temp_string)/1000
			#print(temp_c)
			measurementRecord = (f'{datetime.datetime.today().strftime("%Y-%m-%d")}, {datetime.datetime.now().strftime("%H:%M:%S")}, {int(lightval)}, {temp_c}')
			print(measurementRecord)
			outputfile.write(measurementRecord+"\n")

