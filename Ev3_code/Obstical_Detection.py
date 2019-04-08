#!/usr/bin/env python3
# So program can be run from Brickman

from ev3dev.ev3 import *
from time import sleep
from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds




def Claw(motion):
    #declares claw object
    clawm = MediumMotor(OUTPUT_B)


    if(motion==1):
        #Runs claw for a time amount for it tighten
        clawm.run(time_sp=1500, speed_sp=-750)
        Claw(0)

    #Opens the claw
    if(motion==0):
        clawm.run(time_sp=3000, speed_sp=750)
        Claw(1)

    return 0
    


