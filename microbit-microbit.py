# USE: https://createai.microbit.org/code
        # Example with model including actions:
        # nothing, movemement & walking

def on_on_start():
    basic.show_icon(IconNames.HOUSE)
ml.on_start(ml.event.nothing, on_on_start)

def on_on_start2():
    basic.show_icon(IconNames.CONFUSED)
ml.on_start(ml.event.movement, on_on_start2)

def on_on_start3():
    basic.show_icon(IconNames.YES)
    radio.send_string("Walking")
ml.on_start(ml.event.walking, on_on_start3)

def on_button_pressed_a():
    radio.send_string("" + str((input.temperature())))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_string("" + str((input.light_level())))
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)
basic.show_icon(IconNames.HEART)
