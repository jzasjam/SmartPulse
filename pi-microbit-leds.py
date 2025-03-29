# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# COMMUNICATE WITH THE MICROBIT (FROM THE RASPBERRY PI)
    # + Lighet LEDS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import serial
import time
from gpiozero import LED

green = LED(4)      # LED with reference to GPIO Pin
yellow = LED(17)
red = LED(27)
  
## Edit the line below to the correct port
PORT = "/dev/ttyACM0"
BAUD = 115200

# Open serial connection once
s = serial.Serial(PORT, baudrate=BAUD, parity=serial.PARITY_NONE,
                  stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

time.sleep(2)  # Give some time for connection to establish


message = "Hi from Pi"  # Message to send to micro:bit
s.write(message.encode('utf-8'))  # Serial write the message encoded
print('Send to micro:bit '+message) # Output to console

# Listen for messaged from micro:bit
while True:

    time.sleep(1)  # Delay to prevent spamming micro:bit


    # Check if the MicroBit sent a message back
    if s.in_waiting > 0:  # Check if there's data available
        received = s.readline().decode("utf-8", errors="ignore").strip()  # Read & decode
        print("MicroBit says:", received)  # Print the received message
        green.on() 
        time.sleep(0.25)
        green.off() 
        yellow.on() 
        time.sleep(0.25)
        yellow.off() 
        red.on() 
        time.sleep(0.25)
        red.off() 


