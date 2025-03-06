"""
BASELINE ALGORITHM:

Curtain is closing if not sunny (light > 15) for 30 mins, temperature dropped by 0.5 K in 30 min and it is the afternoon, or if it is close to sunset.  

"""

import queue
import time
from datetime import datetime

q = queue.Queue()

curtainClosed = True

with open("TempLog/20250223.csv") as file, open("closingTimes.txt", 'w') as outFile:

	secondsWithoutSun = 0

	for i,line in enumerate(file):	
		
		values = line[0:-1].split(",")

		#if i>20000:
		#	break


		try:
			temp, light = float(values[3][0:-1]), int(values[2])
		except ValueError:
			print("ValueError")
			continue

		if q.qsize() <= 1800:
			q.put(temp)

		itIsSunnyNow = light < 15

		if not itIsSunnyNow:
			secondsWithoutSun += 1
		else:
			secondsWithoutSun = 0

		print(i, values, "qsize:", q.qsize())
		timeLogged = datetime.strptime(values[1], " %H:%M:%S")
		
		print(timeLogged)	

		if curtainClosed and timeLogged.hour == 8:
			curtainClosed = False

		if q.qsize()>1790:
			temp1800secondsAgo = q.get()
			currentTemperature = temp

			temperatureDroppedByHalfKelvin = currentTemperature + 0.5 < temp1800secondsAgo
			print("temperatureDroppedByHalfKelvin ", temperatureDroppedByHalfKelvin, " currentTemperature ", currentTemperature, " temp1800secondsAgo ", temp1800secondsAgo)


			if not curtainClosed and timeLogged.hour >= 12:
					
					
					itWasntSunnyFor1800seconds = secondsWithoutSun >= 1800

					if itWasntSunnyFor1800seconds and temperatureDroppedByHalfKelvin:
						print("Closing now!")
						time.sleep(5)
						curtainClosed = True
						outFile.write(values[0] + values[1] + "\n")

#			if light > 15 and temp + 0.5 > 
			#...
		#elif timeLogged.hour >= 16