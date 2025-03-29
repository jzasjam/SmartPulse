from sense_hat import SenseHat
from azure.iot.device import IoTHubDeviceClient, Message, ProvisioningDeviceClient
import time
import json

# Azure IoT Central credentials (Replace with your actual values)
ID_SCOPE = "0ne00ED695A"
DEVICE_ID = "smartpulsepi"
DEVICE_KEY = "qHBiek1nfggaEWKvamF3+VpXIZA6J3xVoyrqpShKd7w="

# Global endpoint for Azure DPS
DPS_ENDPOINT = "global.azure-devices-provisioning.net"

# Initialize Sense HAT
sense = SenseHat()

# Function to provision the device and get the IoT Hub connection string
def provision_device():
    provisioning_client = ProvisioningDeviceClient.create_from_symmetric_key(
        provisioning_host=DPS_ENDPOINT,
        registration_id=DEVICE_ID,
        id_scope=ID_SCOPE,
        symmetric_key=DEVICE_KEY
    )
    
    registration_result = provisioning_client.register()
    
    if registration_result.status == "assigned":
        return f"HostName={registration_result.registration_state.assigned_hub};DeviceId={DEVICE_ID};SharedAccessKey={DEVICE_KEY}"
    else:
        raise Exception("Device provisioning failed!")

# Get IoT Hub connection string
CONNECTION_STRING = provision_device()

# Create IoT Hub client
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def send_data():
    try:
        while True:
            # Read sensor data
            temperature = sense.get_temperature()
            humidity = sense.get_humidity()
            pressure = sense.get_pressure()

            # Create JSON payload
            msg = {
                "temperature": round(temperature, 2),
                "humidity": round(humidity, 2),
                "pressure": round(pressure, 2)
            }

            # Convert to JSON string
            message = Message(json.dumps(msg))
            
            # Send message to Azure IoT Central
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
