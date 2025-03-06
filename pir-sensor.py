from gpiozero import MotionSensor
from datetime import datetime

pir = MotionSensor(4)

while True:
    pir.wait_for_motion()
    now = datetime.now()
    print("You Moved at ", now )
    pir.wait_for_no_motion()
    print("No Motion")
