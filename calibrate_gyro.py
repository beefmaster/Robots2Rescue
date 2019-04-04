#!/usr/bin/env python3
# Calibrate Gyro Sensor

from ev3dev2.sensor.lego import GyroSensor 
from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1

# Connect gyro sensor to any sensor ports
gy = GyroSensor(INPUT_1)
# The gyro is calibrated as soon as it has power
# So if the robot is not perfectly still there will be drift
# Calibrate the gyro and set it up for measuring angles
sound.play_tone(500, 0.5)
gy.mode = 'GYRO-CAL' # Calibrate - Robot must be perfectly still
gy.mode = 'GYRO-ANG' # Angle mode
# Stop program by pressing back button
for i in range(0, 50):
angle = gy.angle
print(str(angle) + ' degrees')
sleep(0.1)