# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# TEST THE SENSE HAT LEDs
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Modified from Source: https://pythonhosted.org/sense-hat 

# Import dependencies
from sense_hat import SenseHat
sense = SenseHat()

# Display A Message on the Sense HAT LEDs
sense.show_message("Hello world!")
