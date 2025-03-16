# The Smart Solar Trap


## Introduction

Sapce heating is one of the biggest energy comsumers in the UK, responsible for about 20% of greenhouse gas emissions. This not only contributes to climate change but also leads to unsustainable expenses for households who need to heat during winter.

People should make more use of solar energy to heat their rooms. The potential is significant, about $1.3 KW/m^2$. Even if only $500 W/m^2$ are captured, this may save up to $5 Kwh$, or the equivalent of 1 Kg of fire wood on a sunny day, for each $m^2$ of south-facing window. 
But what is a low cost way of keeping the heat in after the sun sets and the temperature drops in the afternoon? 

Of course to close the curtains! But many people are not home when it is time to close the curtains. We have the solution...

---

Take a Rasberry Pi, with a light sensor, a temperature sensor, & a motor controller connected.
Well, we didn't have enough money for a stepper motor to control the curtain both ways, so most people wouldn't either, so a servo with a makeshift machanism had to do. 
This means that it only allows for the curtain to be closed, rather than also to be opened. For those who want a fully automated solution without havung to manually reset it, they will have to invest a bit more.

But how do we determine the best time to close the curtains? The answer lies in calculating the heat balance within the room. When the rate of heat loss due to cooling exceeds the rate of heat gain from incoming solar energy, curtains shall close. 

## Data logging

To find an algorithm for optimal closing time, we first had to gather data.
For this, we connected a DS18B20 digital temperature sensor to the Raspi GPIOs. For sensing light, we used a photoresitor circuit. For the latter, we had to convert analog to digital values. The simplest thing to do was connecting the light sensor to an Ardunino Nano, and run a a small program on the Arduino to write analog light readings to the serial interface. The Raspi can then read this from the USB port.

We logged the data from 2025-02-23 10:59 pm to 2025-03-03 07:34 am, when it was mostly sunny in Oxford.

[show plot of logged data. explain: x-Axis time, temperature scale, light level scale, behaviour of temperature/light, ]

This plot shows the temperature and light readings over time. Note that temperature falls over night, rises in the morning from 6am to 8am while the heater is running, and then falls again until the sun kicks in. 
The dashed red lines are our computed curtain closing times for each day. Curtains are closed if the temperature has started to drop for more than 30 minutes and there is not sufficient sunlight to heat the space.

Results appear to be reasonable. 

## Action

Now we also connected a servo to the Raspi GPIO pins to test the curtain closing mechanism. For our demo, we monitor the temperature only for 5 seconds.
One of the issues we had with the servo was that the Raspi doesn't give good signals with the `GPIO.PWM` Python module. The servo was always wiggling. We had to use the `pigpio` package instead. 
[demonstrate]

The installed system combines the code for getting curtain closing time with the code actuating the servo. 

## Future Improvements

While this project is cheap and effective, there are several features that we were unable to implement due to lack of funding. Following are a few of them:

- Cover for hardware: The project is currently a prototype, and requires a cover for all the wires and parts.
- Bi-Directional Control: Using a stepper motor would allow for bi-directional control of the curtains. This means that the user would not have to reset the curtains, and coud run for an extended period without requiring handling.
- Solar-Power: Adding solar panels into the design could provide a self-sufficient power source for the system. 

Once we got to collect more data and know how to process them with machine learning technique, we develop machine learning algorithms that allow the system to continuously improve. Some grown ups have told us we can use reinforcement learning. But we don't know yet if that is nonsense.

