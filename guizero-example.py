# DOCS: https://projects.raspberrypi.org/en/projects/getting-started-with-guis/0

# sudo apt install python3-guizero

from guizero import App, Text

# Starter value
count = 0

# Update the value text
def update_value():
    global count
    count += 1
    value_text.value = count  # Update the text properly

# Set the Window Title
app = App(title="Hello world")
# Set the welcome text
welcome_message = Text(app, text="Welcome to my app")
# Set the value text
value_text = Text(app, text="0")  # Start with 0

# Update the value
app.repeat(1000, update_value)  # Update  the value every 1000ms (1 second)

# Display The App
app.display()
