# Modified from Source: https://gpiozero.readthedocs.io/en/stable/recipes.html#led 

from gpiozero import LED
from time import sleep

green = LED(4)      # LED with reference to GPIO Pin
yellow = LED(17)
red = LED(27)

green.on()          # Turn on the LED
sleep(0.5)
yellow.on()
sleep(0.5)
red.on()
sleep(0.5)

while True:
    
    green.toggle()  # Toggle the LED state
    sleep(0.5)
    yellow.toggle()
    sleep(0.5)
    red.toggle()
    sleep(0.5)
