# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# GET THE LDR (Light Dependant Resistor) LIGHT EVENTS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from gpiozero import LightSensor

sensor = LightSensor(18)

# Detect when it is light or dark
print("Press Ctrl+C To Stop")

while True:
	sensor.wait_for_light()
	print("It's light! :)") # Print a notification
	print(sensor.value)	# Print the value (between 0-1)
	
	sensor.wait_for_dark()
	print("It's dark :(")
	print(sensor.value)
