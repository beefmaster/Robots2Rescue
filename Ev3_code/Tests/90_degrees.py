#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

ts = TouchSensor(INPUT_1)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_D)

while True:
    if ts.is_pressed:
        steering_drive.on_for_rotations(-50, SpeedPercent(50), 2/3)
    else:
        steering_drive.on_for_rotations(0, SpeedPercent(0), 0)