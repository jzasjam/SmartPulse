# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# USE THE CAMERA FOR AI IMAGE RECOGNITION
    # with a Teachable Machine model
    # and light up LEDs depending on predicted class
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Import required libraries
import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
from picamera2 import Picamera2
from gpiozero import LED

model_directory = "camera-ai"

# Define the LED pins (by GPIO reference)
green = LED(4)
yellow = LED(17)
red = LED(27)

# Load Teachable Machine model
model_path = model_directory+"/model_unquant.tflite"  # Update with your model's path
interpreter = tflite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Load labels from labels.txt
with open(model_directory+"/labels.txt", "r") as f:  # Update with correct path to labels.txt
    labels = [line.strip() for line in f.readlines()]

# Initialize Picamera2 (Arducam)
picam2 = Picamera2()
config = picam2.create_still_configuration()
picam2.configure(config)

# Enable Auto White Balance (AWB) to fix colors
picam2.set_controls({"AwbMode": 1})  # 1 = Auto white balance

# Set up OpenCV window size
window_width = 640  # Adjust the window size as desired
window_height = 480  # Adjust the window size as desired
cv2.namedWindow("Preview", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Preview", window_width, window_height)

# Start the camera (without using preview)
picam2.start()

try:
    while True:
        # Capture frame manually from Picamera2
        frame = picam2.capture_array()  # Capture frame as a numpy array

        # Convert from BGR to RGB (to fix color issues)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Resize and preprocess the image for the model
        img_resized = cv2.resize(frame, (224, 224))  # Resize to model input size
        img_resized = np.expand_dims(img_resized, axis=0).astype(np.float32) / 255.0  # Normalize
        
        # Run inference on the current frame
        interpreter.set_tensor(input_details[0]['index'], img_resized)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])
        predicted_class = np.argmax(output_data)

        # Get the label from the labels list
        predicted_label = labels[predicted_class]

        # Debugging: Print the predicted label and confidence
        print(f"Predicted Class: {predicted_class} ({predicted_label})")
        print(f"Confidence: {output_data[0][predicted_class]:.4f}")
        
        # Change LED status depending on predicted class
        green.off()
        yellow.off()
        red.off()
        if(predicted_class==0):
                green.on()
        if(predicted_class==1):
                yellow.on()
        if(predicted_class==2):
                red.on()
        
        # Overlay predicted label on the frame
        cv2.putText(frame, f"Class: {predicted_label}", (100, 350),
                    cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 255, 0), 10)

        # Display the frame with the prediction
        cv2.imshow("Preview", frame)
        
        # Wait for user input (press 'q' to quit)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # Press 'q' to quit
            break

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Stop the camera and close OpenCV windows
    picam2.stop()
    cv2.destroyAllWindows()
    print("Camera stopped.")
