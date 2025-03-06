# Modified from Source: https://pythonhosted.org/sense-hat 


# Import dependencies
from sense_hat import SenseHat

# Define a function to call when the joystick is pressed up
def pushed_up(event):
	print(event)
	
# Initialise the event handler for joystick pressed up
sense.stick.direction_up = pushed_up


# Define a function to call when the joystick is pressed in any direction
def do_thing(event):
      if event.action == 'pressed':
          print(f'You pressed {event.direction}')
          if event.direction == 'up':
              print('Up')
          elif event.direction == 'down':
              print('Down')
      elif event.action == 'released':
          print(f'You released {event.direction}')

# Initialise the event handler for joystick pressed in any direction
sense.stick.direction_any = do_thing
