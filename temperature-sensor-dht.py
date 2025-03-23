# FOR USE WITH THE SEEED STUDIO DHT11 TEMPERATURE & HUMIDITY SENSOR DHT11
# Source: https://pimylifeup.com/raspberry-pi-dht11-sensor

import time
import adafruit_dht
import board

dht_device = adafruit_dht.DHT11(board.D14) # Set the GPIO pin (eg. D4 = GPIO4)

while True:
    try:
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9 / 5) + 32

        humidity = dht_device.humidity

        print("Temp:{:.1f} C / {:.1f} F    Humidity: {}%".format(temperature_c, temperature_f, humidity))
    except RuntimeError as err:
        print(err.args[0])

    time.sleep(2.0)
