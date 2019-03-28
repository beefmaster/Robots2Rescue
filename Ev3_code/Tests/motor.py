#!/usr/bin/env python3
# So program can be run from Brickman

from ev3dev.ev3 import *
from time import sleep
m = LargeMotor('outB')
l = LargeMotor('outA')
btn = 1
while(tmp==1):
    m.run_to_rel_pos(position_sp=1000, speed_sp=900, stop_action="hold")
    print("set speed (speed_sp) = " + str(m.speed_sp))
    print("actual speed = " + str(m.speed))
