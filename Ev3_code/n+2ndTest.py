#!/usr/bin/env python3

from ev3dev2.motor import (OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, MediumMotor,
                           MoveSteering, SpeedPercent)
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor



medMotor = MediumMotor(OUTPUT_C)
ultrasonic_sensor_front = UltrasonicSensor(INPUT_4)
ultrasonic_sensor_side = UltrasonicSensor(INPUT_2)
ultrasonic_sensor_front.mode = 'US-DIST-CM'
ultrasonic_sensor_side.mode = 'US-DIST-CM'
gyro = GyroSensor(INPUT_1)
gyro.mode = GyroSensor.MODE_GYRO_ANG


drivetrain = MoveSteering(OUTPUT_D, OUTPUT_B)



while True:
    if ultrasonic_sensor_front.distance_centimeters <= 10:
        if ultrasonic_sensor_side.distance_centimeters <= 15:
            drivetrain.on(steering = -100, speed = 20)
            gyro.wait_until_angle_changed_by(90)
            drivetrain.on(steering = 0, speed = 0)

        else:
            drivetrain.on(steering = 100, speed = 20)
            gyro.wait_until_angle_changed_by(90)
            drivetrain.on(steering = 0, speed = 0)

    else:
        drivetrain.on(steering = 0, speed = 20)



medMotor.on_for_rotations(SpeedPercent(50), 2)

