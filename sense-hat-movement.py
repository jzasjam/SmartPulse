# Modified from Source: https://pythonhosted.org/sense-hat 

# Import dependencies
from sense_hat import SenseHat
import time

# Initialise Sense HAT 
sense = SenseHat()

# Loop to continuously check sensor values
while(True):
	
	# Get the movement (pitch, roll & yaw) values from the accelerometer
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

	# Print the accelerometer values
	print("x={0}, y={1}, z={2}".format(x, y, z))
