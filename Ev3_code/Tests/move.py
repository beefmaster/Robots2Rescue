#!/usr/bin/env python3
# So program can be run from Brickman

from ev3dev.ev3 import *
from time import sleep
from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds


m = MediumMotor('outB')
btn = 1
tmp = 1

while(True):
    m.run_to_rel_pos(position_sp=1000, speed_sp=900, stop_action="hold")
    print("set speed (speed_sp) = " + str(m.speed_sp))
    print("actual speed = " + str(m.speed))
