# Construction

## Parts

- Servo
- Weight
- Fishing Wire
- Pulley and a suitable Axle
- DS18B20 Temperature Sensor
- LDR Photo Resistor (Light Sensor)
- Raspberry Pi
- Arduino Nano
- Micro SD Card
- Wires
- Hot Glue Gun

## Assembly

### Release System

- Attach the pulley to one end of the curtain railing so that it is perpendicular to the movement of the curtain.
- Use fishing wire to connect the end of curtain to the weight through the pulley, then create a loop further along to hook the servo to.

- Use hot glue to secure the servo motor to the model stand just below, but not in the way of, the pulley.
- Ensure the servo arm can move freely to release the weight.


### Wiring

#### Sensors

- Connect the VCC pin of the DS18B20 to Pin 1  on the Raspberry Pi (RPi).
- Connect the GND pin of the DS18B20 to Pin 6.
- Connect the data pin of the DS18B20 to the GPIO7.
- Enable the 1-wire protocol on the RPi: https://www.raspberrypi-spy.co.uk/2018/02/enable-1-wire-interface-raspberry-pi/, which is used by the temperature sensor.
 
- Connect the VCC on the LDR Light Sensor to 5V on the Arduino Nano.
- Connect the two GND's together.
- Connect the AO (Analog Output) on the LDR to the A5 pin.

#### Servo

- Once the servo is attached, connect the GND (negative) wire to pin 20 on the RPi.
- Attach the VCC (positive) wire to pin 17 on the RPi.
- Connect the sig wire to pin 16 on the RPi

#### Arduino Nano

- Once the above steps have been completed, attach the Arduino Nano to the RPi via USB cable. Upload `LightSensorTest.ino` to the Arduino Nano.
