import serial, termios

with serial.Serial('/dev/ttyUSB0', 9600, timeout=2) as ser:
  while True:
    try:
        
        s = ser.readline()        # read up to five bytes (timeout)
        #..     line = ser.readline()   # read a '\n' terminated line
        try:
            lightval = int(s.decode("utf-8"))
        except ValueError as ex:
            lightval = 0
        print(lightval)
    except serial.serialutil.SerialException as ex:
        print(ex)
    except termios.error as ex:
        print(ex)
