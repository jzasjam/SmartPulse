# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# SEND RASPBERRY PI SENSE HAT DATA TO A AZURE IOT HUB
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from sense_hat import SenseHat
from azure.iot.device import IoTHubDeviceClient, Message
import time

# Replace with your actual IoT Hub device connection string
# Example: 
# CONNECTION_STRING = "HostName=your-iot-hub.azure-devices.net;DeviceId=your-device-id;SharedAccessKey=your-device-key"
CONNECTION_STRING = ""

# Initialize Sense HAT and IoT client
sense = SenseHat()
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def send_data():
    try:
        while True:
            # Read sensor data
            temperature = sense.get_temperature()
            humidity = sense.get_humidity()
            pressure = sense.get_pressure()

            # Create message payload
            msg = {
                "temperature": round(temperature, 2),
                "humidity": round(humidity, 2),
                "pressure": round(pressure, 2)
            }

            # Convert to JSON string
            message = Message(str(msg))

            # Send message to Azure IoT Hub
            print(f"Sending message: {msg}")
            client.send_message(message)
            print("Message sent successfully!")

            time.sleep(5)  # Adjust interval as needed

    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        client.shutdown()

if __name__ == "__main__":
    send_data()
