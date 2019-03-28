#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor, OUTPUT_B
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.led import Leds

# Program to control movement of arm with medium motoR

medium_motor = MediumMotor(OUTPUT_B)
#inversed = POLARITY_INVERSED
#medium_motor.polarity = inversed
#medium_motor.mode = 'COMMAND_RUN_TIMED'

medium_motor.on_for_seconds(20, 5)
