#!/usr/bin/env python3
"""
Test program 1 of R2R project;
in one-script format.

"""
from ev3dev2.motor import (
    MoveSteering, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C)
from ev3dev2.sensor import INPUT_1, INPUT_2,INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor.lego import ColorSensor

# Imports from plugin.

ultrasonic_sensor = UltrasonicSensor(INPUT_4)
# define ultrasonic sensor.

gyro = GyroSensor()
gyro.mode = GyroSensor.MODE_GYRO_ANG
# define gyro sensor;
# set gyro sensor to detect angles.


color_sensor = ColorSensor(INPUT_3)
color_sensor.mode = 'COL-COLOR'
# definr color sensor;
# put color sensor in COL-COLOR mode.

colors = ('red', 'blue')
# 0: No color   1: Black   2: Blue   3: Green   
# 4: Yellow   5: Red   6: White   7: Brown

drivetrain = MoveSteering(OUTPUT_B, OUTPUT_C)
# control drivetrain motors usinf Sterring Drive.

medium_motor = MediumMotor(OUTPUT_A)
# control the medium motor of victim intake mechanics. 

drivetrain.on(steering=0, speed=20)

while ultrasonic_sensor.distance_centimeters < 2.0:
    drivetrain.on(steering=0, speed=0)
    if color_sensor.color == 5:
        # set this color to victim color;
        medium_motor.on_for_degrees(speed=-10, degrees=90)
        # lower arm;
        drivetrain.on_for_seconds(steering=0, speed=-20, seconds=2)
        # drive back for 2 seconds;
        medium_motor.on_for_degrees(speed=10, degrees=90)
        # raise arm.

    elif color_sensor.color == 2:
        # set this color to color of wall;
        drivetrain.on(steering=-100, speed=5)
        gyro.wait_until_angle_changed_by(180)
        drivetrain.off()
        # turn around
        drivetrain.on(steering=0, speed=20)
        # drive away at speed of 20


"""
drivetrain.on(steering=-100, speed=5)
gyro.wait_until_angle_changed_by(90)
drivetrain.off()

# turn left 90 degrees using gyro sensor; 
# to turn right, change steering to 100.
"""

