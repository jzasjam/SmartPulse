# USE: https://createai.microbit.org/code
        # Example with model including action: walking

radio.set_group(1)
basic.show_icon(IconNames.HEART)

def on_on_stop():
    basic.show_icon(IconNames.NO)
    radio.send_string("Stopped Walking")
ml.on_stop(ml.event.walking, on_on_stop)

def on_on_start():
    basic.show_icon(IconNames.YES)
    radio.send_string("Walking")
ml.on_start(ml.event.walking, on_on_start)

def on_button_pressed_a():
    radio.send_string("" + str((input.temperature())))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_string("" + str((input.light_level())))
input.on_button_pressed(Button.B, on_button_pressed_b)