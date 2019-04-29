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


while True:


        # if the robot keeps spinning and won't stop, set to rotate for a few seconds.
	    if cl.color == 5:
	        tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(0), 5)
	       
	        # change LED colours to green if a true victim is detected
	        leds.set_color("LEFT", "GREEN")
                leds.set_color("RIGHT", "GREEN")

	
	
	    elif cl.color == 2:
	        tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(0), 5)

	        leds.set_color("LEFT", "RED")
	        leds.set_color("RIGHT", "RED")
        else :
            tank_drive.on(SpeedPercent(50), SpeedPercent(0))
            
