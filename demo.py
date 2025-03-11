"""
BASELINE ALGORITHM:

Curtain is closing if not sunny (light > 15) for 30 mins, temperature dropped by 0.5 K in 30 min and it is the afternoon, or if it is close to sunset.  

CLI PARAMETER:
- Earliest close time
- Latest close time
- Temperature trigger difference
- Temperature trigger time
- Light level sunny
- Light level trigger time
- MAYBE: Data source (file or default read from sensor)
- 
"""

import os
import glob
import queue
import argparse
import time
import math
import datetime
import serial
import RPi.GPIO as GPIO
from datetime import datetime

parser = argparse.ArgumentParser(
	prog='Curtain Closer',
	description='Main program for Curtain Closer.',
	)
parser.add_argument('-b', '--beginning', nargs='?', const="", help="Earliest closing time", default=12)
parser.add_argument('-e', '--end', nargs='?', const="", help="Latest closing time", default=17)
parser.add_argument('-t', '--tempTrigger', nargs='?', const="", help=" Temperature trigger difference in K", default=0.5)
parser.add_argument('-l', '--lightTrigger', nargs='?', const="", help="Max value for light level to be considered sunny", default=15)
parser.add_argument('--triggerTime', nargs='?', const="", help="History in seconds for trigger", default=5)

args = parser.parse_args()


q = queue.Queue()

curtainClosed = True
servoPin = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin, GPIO.OUT)

p = GPIO.PWM(servoPin, 50)
p.start(2.5)

device_file = '/sys/bus/w1/devices/28-3fa9d445207e/w1_slave' 
date = str(datetime.datetime.today().strftime("%Y %m %d"))

def set_angle(angle, pwm, delay = 0.1):
	duty = angle / 18 + 2
	pwm.ChangeDuty(duty)
	time.sleep(delay)


with open(device_file, 'r') as file, open('sensorLog.txt', 'w') as outFile, serial.Serial('/dev/ttyUSB0', 9600, timeout = 2) as ser:

	secondsWithoutSun = 0

	while True:
		lines = file.readlines()
		light = ser.readline().decode('utf-8')
		ser.reset_input_buffer()
		file.seek(0)
		time.sleep(1)
		try:
			equals_pos = lines[1].find('t=')
		except IndexError:
			print("I",end=' ')
			continue
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			temp = float(temp_string)/1000
			measurementRecord = (f'{datetime.datetime.today().strftime("%Y-%m-%d")}, {datetime.datetime.now().strftime("%H:%M:%S")}, {int(lightval)}, {temp}')
			outFile.write(measurementRecord+"\n")

			if q.qsize() <= args.triggerTime:
				q.put(temp)
			
			itIsSunnyNow = light < args.lightTrigger

			if not itIsSunnyNow:
				secondsWithoutSun += 1
			else:
				secondsWithoutSun = 0

			print(i, values, "qsize:", q.qsize())
			timeLogged = datetime.strptime(values[1], " %H:%M:%S")
			
			print(timeLogged)	

			if curtainClosed and timeLogged.hour == 8:
				curtainClosed = False

			if q.qsize()>args.triggerTime-1:
				tempNsecondsAgo = q.get()
				currentTemperature = temp

				temperatureDroppedByHalfKelvin = currentTemperature + args.tempTrigger < tempNsecondsAgo
				print("temperatureDroppedByHalfKelvin ", temperatureDroppedByHalfKelvin, " currentTemperature ", currentTemperature, " tempNsecondsAgo ", tempNsecondsAgo)


				if not curtainClosed and timeLogged.hour >= args.beginning:
						
						
					itWasntSunnyForNseconds = secondsWithoutSun >= args.triggerTime

					if itWasntSunnyForNseconds and temperatureDroppedByHalfKelvin:
						print("Closing now!")
						set_angle(180, p, 1)
						set_angle(45, p)
						time.sleep(5)
						curtainClosed = True
						outFile.write(values[0] + values[1] + "\n")

#			if light > 15 and temp + 0.5 > 
			#...
		#elif timeLogged.hour >= 16