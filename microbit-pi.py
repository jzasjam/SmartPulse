# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  CODE FOR MICROBIT COMMMUNICATING WITH THE RASPBERRY PI
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# USE: https://python.microbit.org/v/3

from microbit import *
import radio

# Initialize UART/Serial Connection for Pi communication
uart.init(baudrate=115200)  # Match with Pi's baud rate

# Initialize the radio
radio.config(group=1, power=7)  # Use a specific channel & max power
radio.on()

while True:
    sleep(500)

    # Listen for messages
    bytestring = uart.readline()
    display.show(Image.HEART) # Display the listener is ready

    # If there is a message from the Raspberry Pi
    if bytestring:
        display.show(Image.ARROW_S) # Display thinking aboutn message
        sleep(400)
        try:
            message = bytestring.decode("utf-8").strip()  # Decode and remove \n
            print("Received:", message)  # This is returned to the Raspberry Pi terminal
            
            #display.scroll(message)  # Scroll the message on the LEDs
            
            display.show(Image.HAPPY) # Display message received
            sleep(400)
        except Exception as e:
            print("Decode error:", e)  # This is returned to the Raspberry Pi terminal
            display.show(Image.SAD) # Display message error
            sleep(400)

    # Read from radio (Other Microbit -> Microbit)
    radio_message = radio.receive()

    if radio_message:
        print("Received from radio:", radio_message)  # Show received radio message
        uart.write(radio_message)  # Send to Pi
        display.show(Image.ARROW_N)
        sleep(400)
    
    # If button A is pressed, send a message back to the Raspberry Pi
    if button_a.was_pressed():
        uart.write("Button A Pressed\n")
        display.show("A")
        sleep(400)


