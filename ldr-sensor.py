# Source: Modified from https://gpiozero.readthedocs.io/en/latest/recipes.html#light-sensor 

from gpiozero import LightSensor
import time

sensor = LightSensor(18)

# Continuously detect light level
print("Press Ctrl+C To Stop")

while True:
	time.sleep(0.1) # Small delay between readings
	print(sensor.value)
