#!/usr/bin/env python3
# So program can be run from Brickman

from ev3dev2.motor import (OUTPUT_A, OUTPUT_B, OUTPUT_D, MediumMotor,
                           MoveSteering, SpeedPercent)
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor




ultrasonic_sensor_front = UltrasonicSensor(INPUT_4)
ultrasonic_sensor_side = UltrasonicSensor(INPUT_2)
ultrasonic_sensor_front.mode = 'US-DIST-CM'
ultrasonic_sensor_side.mode = 'US-DIST-CM'
gyro = GyroSensor(INPUT_1)
gyro.mode = GyroSensor.MODE_GYRO_ANG


drivetrain = MoveSteering(OUTPUT_D, OUTPUT_B)

##make a slight turn when right hand side sensor comes close to a wall
while ultrasonic_sensor_front.distance_centimeters>10:
    drivetrain.on(steering=0, speed=80)

if ultrasonic_sensor_front.distance_centimeters<10:
    drivetrain.on(steering=0, speed=0)


    
