# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# DETECT THE SENSE HAT TEMPERATURE
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Modified from Source: https://pythonhosted.org/sense-hat 

# Import dependencies
from sense_hat import SenseHat

# Initialise Sense HAT 
sense = SenseHat()

# Get the Temperature
temp = sense.get_temperature()
print(f"Temperature: {temp} C")

# Get the Humidity
humidity = sense.get_humidity()
print(f"Humidity: {humidity} %")

# Get the Pressure
pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)
