import db
import adafruit_dht
import time
from board import D2 

# Check for your sensor pin
# Import it above and replace below
_sensor = adafruit_dht.DHT11(D2)

def init():
    print('Initializing sensor DHT11')

def read_sensor():
    while True:
        try:
            humidity = __validateBoundaries(_sensor.humidity, 0, 100)
            temperature = __validateBoundaries(_sensor.temperature, 0, 125)
            if humidity != -255 or temperature != -255:
                db.write_data(temperature, humidity)
            break
        except Exception as e:
            time.sleep(2)
            continue

# Validates if the value is between the boundaries
# to avoid invalid/corrupted data being read
def __validateBoundaries(value, lower, upper):
    if value > lower and value < upper:
        return value
    return -255
