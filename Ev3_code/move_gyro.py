# Move Using Gyro Sensor

import os
import math
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

os.system('setfont Lat15-TerminusBold14') # Large font
# os.system('setfont Lat15-TerminusBold32x16') # Very large font

# =======================================================================
# Hardware Definitions
# =======================================================================
# Access the two motors
leftMotor = LargeMotor(OUTPUT_B)
rightMotor = LargeMotor(OUTPUT_D)
print('Motors: Ready')

# The gyro is calibrated as soon as it has power
# So if the robot is not perfectly still there will be drift
# Calibrate the gyro and set it up for measuring angles
gyro = GyroSensor(INPUT_1)
gyro.mode = 'GYRO-CAL' # Calibrate - Robot must be perfectly still
gyro.mode = 'GYRO-ANG' # Angle mode
print('Gyro Sensor: Calibrated')

# =======================================================================
# Main Procedure
# =======================================================================
# Initialise the target motion
# Move forward while turning 20deg clockwise, then straight
forwardSpeed = 30
targetAngle = gyro.angle + 20

# Main program loop
# Pressing the Back button will halt the program
halt = False
while not halt:

# Read the Gyro and calulate error
gyroError = targetAngle - gyro.angle
print(gyroError)

# Calulate the differential between motor speeds
if abs(gyroError) < 2.5:
differential = 0
else:
differential = 2 * gyroError
# Make sure the differentialis are not too wild
# If you want the robot to spin then max(differential) >= 2 * forwardSpeed
differential = min(max(differential, -60), 60)

# Calculate the motor speeds
lmSpeed = forwardSpeed + differential / 2
rmSpeed = forwardSpeed - differential / 2

# Make sure the motor speeds are not too wild
lmSpeed = min(max(lmSpeed, -50), 50)
rmSpeed = min(max(rmSpeed, -50), 50)

# Set motor speeds for this iteration of the loop
# motor.on(speed) turn the motor on for ever, so don't forget to stop
leftMotor.on(lmSpeed)
rightMotor.on(rmSpeed)
print(lmSpeed, ', ', rmSpeed)

# Small delay to help read screen print, too slow and the robot motion will be jerky
sleep(0.2)