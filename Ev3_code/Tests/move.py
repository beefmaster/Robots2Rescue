#!/usr/bin/env python3
# So program can be run from Brickman

from ev3dev2.ev3 import *
from time import sleep
from ev3dev2.motor import MediumMotor, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds


m = MediumMotor(OUTPUT_C)


while(True):
    m.run_to_rel_pos(position_sp=1000, speed_sp=900, stop_action="hold")
   
