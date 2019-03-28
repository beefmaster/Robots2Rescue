#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from time import sleep

from ev3dev.ev3 import *
from time   import sleep
m = LargeMotor('outB')
l = LargeMotor('outC')




while True:
    m.run_forever(speed_sp=500) 
    l.run_forever(speed_sp=450)
    # equivalent to power=20 in EV3-G
    sleep(5)
    m.stop(stop_action="coast")
    l.stop(stop_action="coast")
    sleep(4)


    sleep(5)
    m.stop()
    l.stop()
