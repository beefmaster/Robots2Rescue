#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_3
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds

# program for colour sensor to detect red (true) and blue (false) victims
# attach colour sensor to port 3

cl = ColorSensor(INPUT_3)
leds = Leds()

# put color sensor in COL-COLOR mode 
cl.mode = 'COL-COLOR'

colors = ('red', 'blue')

while True:
    if cl.color == 5:
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "RED")
    
    elif cl.color == 2:
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "GREEN")