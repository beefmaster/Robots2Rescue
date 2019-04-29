#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.led import Leds

# Program to go straight approximately 60cm

tank_drive = MoveTank(OUTPUT_B, OUTPUT_D)
tank_drive.on(SpeedPercent(50), SpeedPercent(50))

