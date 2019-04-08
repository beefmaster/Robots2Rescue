straight_drive()
while True:
    if ultrasonic_sensor_front.distance_centimeters <= 2.0:
        stop_drive()
        #stop robot if something is at front.

        if ultrasonic_sensor_side.distance_centimeters <= 5.0:
            left_turn()
            
        elif ultrasonic_sensor_side.distance_centimeters > 5.0:
            right_turn()
         
    else:
        straight_drive()
        
    # use with functions.
