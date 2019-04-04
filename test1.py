"""
Test program 1 of R2R project;
in one-script format.
"""
from ev3dev2.motor import (OUTPUT_A, OUTPUT_B, OUTPUT_C, MediumMotor,
                           MoveSteering)
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import (ColorSensor, GyroSensor,
                                 UltrasonicSensor)

ultrasonic_sensor_front = UltrasonicSensor(INPUT_4)
ultrasonic_sensor_side = UltrasonicSensor(INPUT_2)
# define ultrasonic sensor.

gyro = GyroSensor()
gyro.mode = GyroSensor.MODE_GYRO_ANG
# define gyro sensor;
# set gyro sensor to detect angles.


color_sensor = ColorSensor(INPUT_3)
color_sensor.mode = 'COL-COLOR'
# definr color sensor;
# put color sensor in COL-COLOR mode.

colors = ('red', 'white')
# 0: No color   1: Black   2: Blue   3: Green   
# 4: Yellow   5: Red   6: White   7: Brown

drivetrain = MoveSteering(OUTPUT_B, OUTPUT_C)
# control drivetrain motors usinf Sterring Drive.

medium_motor = MediumMotor(OUTPUT_A)
# control the medium motor of victim intake mechanics. 

drivetrain.on(steering=0, speed=20)

while ultrasonic_sensor_front.distance_centimeters < 2.0:
    drivetrain.on(steering=0, speed=0)
    #stop robot if something is at front.

    if color_sensor.color == 5:
        # set this color to victim color;
        medium_motor.on_for_degrees(speed=-10, degrees=90)
        # lower arm;
        drivetrain.on_for_seconds(steering=0, speed=-20, seconds=2)
        # drive back for 2 seconds;
        medium_motor.on_for_degrees(speed=10, degrees=90)
        # raise arm.
        drivetrain.on(steering = 0, speed = -20)
        
        drivetrain.on_for_seconds(steering = 100, speed = 20)
        gyro.wait_until_angle_changed_by(360)
        #rotate and check if victim is picked up (for 1 rotation).

        while drivetrain.on:
            if color_sensor == 5:
                # set this color to victim color;
                medium_motor.on_for_degrees(speed=-10, degrees=90)
      
                drivetrain.on_for_seconds(steering=0, speed=-20, seconds=2)
                # drive back for 2 seconds;
                medium_motor.on_for_degrees(speed=10, degrees=90)
                # raise arm.
                drivetrain.on_for_seconds(steering = 0, speed = -20, seconds=5)
            else :
                drivetrain.on(steering = 0, speed = 0)
        

    elif color_sensor.color == 6:
        # set this color to color of wall (white);
        if ultrasonic_sensor_side.distance_centimeters < 5.0:
            #RHS is wall; turn left, sterring = -100.
            drivetrain.on(steering = -100, speed = 20)
            gyro.wait_until_angle_changed_by(90)
            drivetrain.on(steering = 0, speed = 20)

        elif ultrasonic_sensor_side.distance_centimeters > 5.0:
            #RHS is path; turn right, steering = 100.
            drivetrain.on(steering = -100, speed = 20)
            gyro.wait_until_angle_changed_by(90)
            drivetrain.on(steering = 0, speed = 20)
       






"""
Maze - solving:
we have 2 ultrasonic sensors; one on the fromt and one on the RIGHT side
The side one would follow the wall;
Robot would turn the direction that the sensor detects distance >2cm, or the other way.
"""

"""
drivetrain.on(steering=-100, speed=5)
gyro.wait_until_angle_changed_by(90)
drivetrain.off()
# turn left 90 degrees using gyro sensor; 
# to turn right, change steering to 100.
"""