from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(26)     # Buzzer with reference to the GPIO Pin

while True:
      buzzer.on()       # Turn on Buzzer
      sleep(1)
      buzzer.off()      # Turn off Buzzer
      sleep(1)