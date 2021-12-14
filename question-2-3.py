# Author: ATN 12/14/21

def runway_min():
    acceleration = int(input("Please enter the ship's acceleration: "))
    takeoff_speed = int(input("Please enter the ship's take-off speed: "))
    runway_length = (takeoff_speed ** 2) / (2 * acceleration)
    return runway_length


print("The length of the runway is {0} meters.".format(runway_min()))
