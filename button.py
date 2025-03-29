# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# LIGHT AN LED USING A BUTTON  
# Modified from Source: https://gpiozero.readthedocs.io/en/stable/recipes.html#button-controlled-led
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from gpiozero import LED, Button
from time import sleep

led = LED(20)           # LED with reference to GPIO Pin
button = Button(21)     # Button with reference to GPO Pin

# Function for whan button is pressed
def btnDown():
    print("Button Down")

# Function for when buttion is released
def btnUp():
    print("Button Up")

# Create Event Handlers for functions
button.when_pressed = btnDown
button.when_released = btnUp

# Also, wait for button presses
while True:
    button.wait_for_press() # Wait until button is pressed
    print("Pressed!")
    led.toggle()        # Toggle the LED state
    sleep(0.5)


