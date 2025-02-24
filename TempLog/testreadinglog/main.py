with open("2025-02-17.csv") as file:

	lastTemp, lastLight = -1, -1
	cnt = 0

	nextDay = False
	lastDay = "NA"

	for line in file:

		values = line.split(",");

		try:
			temp, light = float(values[3][0:-1]), int(values[2])
			#print(f"{temp} {light}");
		except ValueError:
			continue

		if lastDay == "NA":
			lastDay = values[0]
		if nextDay:
			if lastDay != values[0]:
				nextDay = False
				lastDay = values[0]
			else:
				continue

		cnt += 1

		if temp < 16 or light > 1000:
			print("Curtain Close at: " + values[1])
			print("Curaint day: " + values[0])
			nextDay = True
		if cnt == 50:
			lastTemp, lastLight = temp, light
			cnt = 0

