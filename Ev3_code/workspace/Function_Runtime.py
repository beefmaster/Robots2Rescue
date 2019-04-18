#!/usr/bin/env python3

from ev3dev2.motor import (
    MoveSteering, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C)
from ev3dev2.sensor import INPUT_1, INPUT_2,INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor.lego import ColorSensor

#defining ultrasonic sensor
ultrasonic_sensor = UltrasonicSensor(INPUT_4)


def disc:
    while ultrasonic_sensor.distance_centimeters < 2.0:
        return 0

    while ultrasonic_sensor.distance_centimeters>2.0:
        return 1


