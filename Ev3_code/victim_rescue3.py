#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.led import Leds

# program for colour sensor to detect red (true) and blue (false) victims
# attach colour sensor to port 3

tank_drive = MoveTank(OUTPUT_B, OUTPUT_D)
us_front = UltrasonicSensor(INPUT_4)
us_side = UltrasonicSensor(INPUT_2)
cl = ColorSensor(INPUT_3)
leds = Leds()
medMotor = MediumMotor(OUTPUT_C)

# put color sensor in COL-COLOR mode
cl.mode = 'COL-COLOR'

# put ultrasonic sensor in distance (cm) mode
us_front.mode = 'US-DIST-CM'
us_side.mode = 'US-DIST-CM'

colors = ('red', 'blue')

while (True):

    if cl.color == 5:
        tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(0), 2)

        # change LED colours to green if a true victim is detected
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "GREEN")

        # lower scoop
        medMotor.polarity = 'inversed'
        medMotor.on_for_rotations(SpeedPercent(50), 2)

        # move robot into position
        tank_drive.on_for_seconds(SpeedPercent(-20), SpeedPercent(-20), 2)
        tank_drive.on_for_rotations(SpeedPercent(20), SpeedPercent(-20), 1/5)
        tank_drive.on_for_seconds(SpeedPercent(20), SpeedPercent(20), 3.5)
        # time of robot driving forward (3.5) needs to be tested to finalize.


        # lift up scoop
        medMotor.polarity = 'normal'
        medMotor.on_for_rotations(SpeedPercent(50), 2)

        # drive back, so that if rescue fails it can start over at original position
        tank_drive.on_for_seconds(SpeedPercent(20), SpeedPercent(20), 3.5)

    elif cl.color == 2:
        tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(0), 2)

        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "RED")

    else:
        tank_drive.on(SpeedPercent(40), SpeedPercent(0))



    # the section below only works if the lifted water bottle blocks the front ultrasonic sensor, which is probably so far the
    # only way of telling whether a victim has been picked up

