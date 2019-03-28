#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

ts = TouchSensor(INPUT_1)
leds = Leds()
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
mB = LargeMotor('outB')
mC = LargeMotor('outC')


while mB.Motor.full_travel_count<3000 & mC.Motor.full_travel_count:
    if ts.is_pressed:
        tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(75), 1)    
    else:
        tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(0), 0)
