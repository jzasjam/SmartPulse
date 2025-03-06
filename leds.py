from gpiozero import LED
from time import sleep

green = LED(4)
yellow = LED(17)
red = LED(27)


while True:
    green.on()
    yellow.on()
    red.on()
