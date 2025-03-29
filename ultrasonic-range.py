# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# USE A ULTRASINIC SENSOR WITH RASPBERRY PI) TO DETECT SOMETHING IN/OUT OF RANGE
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Source: Modified from https://projects.raspberrypi.org/en/projects/physical-computing/12 

from gpiozero import DistanceSensor
from datetime import datetime
import time
  
ultrasonic = DistanceSensor(echo=17, trigger=4, threshold_distance=0.5)


def hello():
    print("Hello")

def bye():
    print("Bye")

ultrasonic.when_in_range = hello
ultrasonic.when_out_of_range = bye
  
while True:
    now = datetime.now()
    ultrasonic.wait_for_in_range()
    print("In range at ", now)
    ultrasonic.wait_for_out_of_range()
    print("Out of range at ", now)
