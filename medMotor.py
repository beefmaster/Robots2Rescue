from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, MediumMotor, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor

medMotor = MediumMotor(OUTPUT_C)
medMotor.on_for_rotations(SpeedPercent(50), 2)
