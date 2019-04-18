#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.led import Leds

# on carpet use this:

    tank_drive = MoveTank(OUTPUT_B, OUTPUT_D)
    tank_drive.on_for_rotations(SpeedPercent(40), SpeedPercent(-40), 41/50)