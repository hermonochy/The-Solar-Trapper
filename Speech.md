# The Smart Solar Trap


## Introduction

Space heating is one of the biggest energy consumers in the UK, responsible for about 20% of greenhouse gas emissions. This not only contributes to climate change but also leads to unsustainable expenses for households who need to heat during winter.

People should make more use of solar energy to heat their rooms. The potential is significant, about $1.3 KW/m^2$. Even if only $500 W/m^2$ are captured, this may save up to $5 Kwh$, or the equivalent of 1 Kg of firewood on a sunny day, for each $m^2$ of a south-facing window. 
But what is a low cost way of keeping the heat in after the sun sets and the temperature drops in the afternoon? 

Of course to close the curtains! But many people are not home when it is time to close the curtains. We have the solution...

---

Take a Raspberry Pi, with a light sensor, a temperature sensor, & a motor controller connected.
Well, we didn't have enough money for a stepper motor to control the curtain both ways, so most people wouldn't either, so a servo with a makeshift mechanism had to do. 
This means that it only allows for the curtain to be closed, rather than also to be opened. For those who want a fully automated solution without having to manually reset it, they will have to invest a bit more.

But how do we determine the best time to close the curtains? The answer lies in calculating the heat balance within the room. When the rate of heat loss due to cooling exceeds the rate of heat gain from incoming solar energy, curtains shall close. 

## Data logging

[show plot of logged data. explain: x-Axis time, temperature scale, light level scale, behaviour of temperature/light, ]
--> Each tick on the x-axis is represents midnight of the respective day. Temperatures are plotted in purple, scale on the right, light levels in green. Lower readings mean more light. Values below 15 are full sun.

To find an algorithm for the most ideal closing time, we needed to gather data first, as it's impractical to test algorithms with live data.

We logged the data from the 23rd of February to the 3rd of March, a time when it was mostly sunny in Oxford.

This plot shows the temperature and light readings over time. Each tick on the x-axis is represents midnight of the respective day. Note that temperature, shown in purple, falls overnight, rises in the morning from 6am to 8am while the heater is running, and then falls again until the sun heats the room later in the morning.

The light values - the green line - are the opposite. During the night, the light value peaks, and stays so for most of the night. Then when the sun comes up, the values suddenly drop. The gradient increases further when the curtains are closed. The values stay at below 20 for most of the day, before increasing again in the evening.

The dashed red lines are our computed curtain closing times for each day. Curtains are closed if the temperature has started to drop for more than 30 minutes and there is not sufficient sunlight to heat the space.

Results appear to be reasonable. 

## Action

Now we also connected a servo to the Raspi GPIO pins to test the curtain closing mechanism. For our demo, we monitor the temperature for only 5 seconds.
One of the issues we had with the servo was that the Raspi doesn't give good signals with the `GPIO.PWM` Python module. The servo was always wiggling. We had to use the `pigpio` package instead. 
[demonstrate]

The installed system combines the code for getting curtain closing time with the code actuating the servo. 

## Future Improvements

It works, but there is still plenty to do:

- For normal users, everything needs to be boxed up to protect the wires.
- Most people cannot work with the command line interface, so the system needs to have a simpler user interface

For use of machine learning, we need to simulate the heat transfer, e.g. with open-meteo data as input. We still have to learn how to do it.

If you are a technical expert, go to https://github.com/Cheney-School/HTM-Solar-Trappers for code and documentation.

Thanks for watching.