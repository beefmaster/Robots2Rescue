#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor, OUTPUT_B, OUTPUT_D, OUTPUT_C, SpeedPercent, MoveTank


medMotor = MediumMotor(OUTPUT_C)

while True:
    medMotor.on_for_rotations(SpeedPercent(-50), -2)