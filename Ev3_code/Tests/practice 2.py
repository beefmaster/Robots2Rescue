#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

# B - left, C- right
# 18 rotations: 3 m

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
#drive robot when touch sensor is pressed.

tank_drive.on_for_rotations(75, 75, 18)
tank_drive.on(SpeedPercent(0), SpeedPercent(0))

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
# drive in a turn for 10 rotations of the outer motor
steering_drive.on_for_rotations(70, SpeedPercent(75), 1.7)
tank_drive.on_for_rotations(75, 75, 18)



# drive classes: tank, steeing, joystick;
# https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/motors.html#multiple-motor-groups
# motor classes: https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/motors.html#units
