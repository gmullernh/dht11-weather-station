# weather-station
Weather Station using Python, Javascript and DHT11 sensor.

## In this project

- Python API that fetches data from DHT11 sensor and saves it to a QuestDB instance.
- The said QuestDB instance.
- A frontend application, made with VueJS (NuxtJS), to visualize the data.

## Running the project

Run the project on a Raspberry Pi, using DHT11 connected to the Digital 2 (D2) port.

Use: `docker compose up --build -d` 

If you're trying to run it on a device other than a RPi, the project will not start, due to the missing pin connection to the `adafruit-circuitpython-dht`.

