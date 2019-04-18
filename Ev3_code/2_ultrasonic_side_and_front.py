#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_4, INPUT_2
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.led import Leds

# Program to control movement of motors with Ultrasonic sensor

tank_drive = MoveTank(OUTPUT_B, OUTPUT_D)
us_front = UltrasonicSensor(INPUT_4)
us_side = UltrasonicSensor(INPUT_2)

us_front.mode = 'US-DIST-CM'
us_side.mode = 'US-DIST-CM'

while True: 
    if us_front.distance_centimeters <= 13 and us_side.distance_centimeters < 10:
        tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(0), 1)
        tank_drive.on_for_seconds(SpeedPercent(-20), SpeedPercent(-20), 1.5)
        tank_drive.on_for_rotations(SpeedPercent(40), SpeedPercent(-40), 42/50)
    elif us_front.distance_centimeters <= 13 and us_side.distance_centimeters > 10:
        tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(0), 1)
        tank_drive.on_for_seconds(SpeedPercent(-20), SpeedPercent(-20), 1.5)
        tank_drive.on_for_rotations(SpeedPercent(-40), SpeedPercent(40), 42/50)
    else:
        tank_drive.on(SpeedPercent(30), SpeedPercent(30))