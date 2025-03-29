# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# COMMUNICATE WITH THE MICROBIT (FROM THE RASPBERRY PI)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import serial
import time

## Edit the line below to the correct port
PORT = "/dev/ttyACM0"
BAUD = 115200

# Open serial connection once
s = serial.Serial(PORT, baudrate=BAUD, parity=serial.PARITY_NONE,
                  stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

time.sleep(2)  # Give some time for connection to establish

while True:
    #message = "Hi"  # Message to send to micro:bit
    #s.write(message.encode('utf-8'))  # Serial write the message encoded
    #print('Send to micro:bit '+message) # Output to console
    time.sleep(1)  # Delay to prevent spamming micro:bit


    # Check if the MicroBit sent a message back
    if s.in_waiting > 0:  # Check if there's data available
        received = s.readline().decode("utf-8", errors="ignore").strip()  # Read & decode
        print("MicroBit says:", received)  # Print the received message


