#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.led import Leds

# Program to control movement of motors with Ultrasonic sensor

tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)
us = UltrasonicSensor(INPUT_4)

us.mode = 'US-DIST-CM'

while True:
    # if distance <= 10cm turn robot left
    if us.distance_centimeters <= 13:
        tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(0), 1)
        tank_drive.on_for_seconds(SpeedPercent(-20), SpeedPercent(-20), 1)
        tank_drive.on_for_rotations(SpeedPercent(25), SpeedPercent(-25), 2/3)
    # continue going straight
    else:
        tank_drive.on(SpeedPercent(50), SpeedPercent(50))