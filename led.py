# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# TEST A SINGLE LED
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Modified from Source: https://gpiozero.readthedocs.io/en/stable/recipes.html#led 

from gpiozero import LED
from time import sleep

led = LED(4)        # LED with reference to the GPIO Pin

led.on()            # Turn on the LED
sleep(0.5)
led.off()           # Turn off the LED
sleep(0.5)

while True:
    
    led.toggle()    # Toggle the LED state (flash)
    sleep(0.5)
