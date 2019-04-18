from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_D, MediumMotor, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor


ultrasonic_sensor_front = UltrasonicSensor(INPUT_4)
ultrasonic_sensor_side = UltrasonicSensor(INPUT_2)
ultrasonic_sensor_front.mode = 'US-DIST-CM'
ultrasonic_sensor_side.mode = 'US-DIST-CM'
# define ultrasonic sensor.

gyro = GyroSensor()
gyro.mode = 'MODE_GYRO_ANG'
# define gyro sensor;
# set gyro sensor to detect angles.


color_sensor = ColorSensor(INPUT_3)
color_sensor.mode = 'COL-COLOR'
# definr color sensor;
# put color sensor in COL-COLOR mode.

colors = ('red', 'white')
# 0: No color   1: Black   2: Blue   3: Green
# 4: Yellow   5: Red   6: White   7: Brown

drivetrain = MoveSteering(OUTPUT_B, OUTPUT_D)
# control drivetrain motors usinf Sterring Drive.

medium_motor = MediumMotor(OUTPUT_A)
# control the medium motor of victim intake mechanics.

def right_turn(drivetrain, gyro):
    drivetrain.on(steering = 100, speed = 10)
    gyro.wait_until_angle_changed_by(90)
    drivetrain.on(steering = 0, speed = 0)

def left_turn(drivetrain, gyro):
    drivetrain.on(steering = -100, speed = 10)
    gyro.wait_until_angle_changed_by(90)
    drivetrain.on(steering = 0, speed = 0)

def stop_drive(drivetrain):
    drivetrain.on(steering = 0, speed = 0)

def straight_drive(drivetrain):
    drivetrain.on(steering = 0, speed = 20)

def rotate_drive(drivetrain, gyro):
    drivetrain.on_for_seconds(steering = 100, speed = 20)
    gyro.wait_until_angle_changed_by(360)
    drivetrain.on(steering = 0, speed = 0)

straight_drive(drivetrain)
while True:
    if ultrasonic_sensor_front.distance_centimeters <= 2.0:
        stop_drive(drivetrain)
        #stop robot if something is at front.

        if ultrasonic_sensor_side.distance_centimeters <= 5.0:
            left_turn(drivetrain, gyro)
            straight_drive(drivetrain)
            
        elif ultrasonic_sensor_side.distance_centimeters > 5.0:
            right_turn(drivetrain, gyro)
            straight_drive(drivetrain)
         
    else:
        straight_drive(drivetrain)
        
    # use with functions.



