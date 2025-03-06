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

import queue
import argparse
import time
from datetime import datetime

parser = argparse.ArgumentParser(
	prog='Curtain Closer',
	description='Main program for Curtain Closer.',
	)
parser.add_argument('-b', '--beginning', nargs='?', const="", help="Earliest closing time", default=12)
parser.add_argument('-e', '--end', nargs='?', const="", help="Latest closing time", default=17)
parser.add_argument('-t', '--tempTrigger', nargs='?', const="", help=" Temperature trigger difference in K", default=0.5)
parser.add_argument('-l', '--lightTrigger', nargs='?', const="", help="Max value for light level to be considered sunny", default=15)
parser.add_argument('--triggerTime', nargs='?', const="", help="History in seconds for trigger", default=1800)

args = parser.parse_args()


q = queue.Queue()

curtainClosed = True

with open("TempLog/20250223.csv") as file, open("closingTimes.txt", 'w') as outFile:

	secondsWithoutSun = 0

	for i, line in enumerate(file):	
		
		values = line[0:-1].split(",")

		#if i>20000:
		#	break


		try:
			temp, light = float(values[3][0:-1]), int(values[2])
		except ValueError:
			print("ValueError")
			continue

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
						time.sleep(5)
						curtainClosed = True
						outFile.write(values[0] + values[1] + "\n")

#			if light > 15 and temp + 0.5 > 
			#...
		#elif timeLogged.hour >= 16