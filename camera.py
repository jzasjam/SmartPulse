# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Take A Picture With The Camera
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from picamera2 import Picamera2
import time

# Initialize camera
picam2 = Picamera2()

# Configure the camera
config = picam2.create_still_configuration()
picam2.configure(config)

# Start camera and take a picture
picam2.start()
time.sleep(2)  # Allow time for auto-exposure to adjust

# Capture The Image
metadata = picam2.capture_file("image.jpg")
print(metadata)

# Stop the camera
picam2.stop()

print("Picture saved as image.jpg") 
