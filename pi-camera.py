
from datetime import datetime

from picamera2 import Picamera2
import time

# Initialize camera
picam2 = Picamera2()

# Configure the camera
config = picam2.create_still_configuration()
picam2.configure(config)


def takePicture():
    # Start camera and take a picture
    picam2.start()
    time.sleep(2)  # Allow time for auto-exposure to adjust
    
    now = datetime.now()
    picname = "image-"+str(now)+".jpg"
    picam2.capture_file(picname)

    # Stop the camera
    picam2.stop()

    print("Picture saved as ", picname)

takePicture()
