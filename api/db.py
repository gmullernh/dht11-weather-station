import psycopg2 as pg
import time

# Connect to an existing QuestDB instance
# Default credentials
conn_str = 'user=admin password=quest host=questdb port=8812 dbname=qdb'

def init():
    print('Initializing db connector')
    is_connected = False

    while is_connected == False:
        try:
            with pg.connect(conn_str) as connection:
                with connection.cursor() as cur:
                    cur.execute('''
                    CREATE TABLE IF NOT EXISTS sensor_data (
                        ts TIMESTAMP,
                        temperature DOUBLE,
                        humidity DOUBLE
                    ) timestamp(ts);
                    ''')
                is_connected = True
        except:
            print('Failed to connect.')
        # Waits 5 seconds and retry
        # since we cannot ensure the database will be
        # running and accepting connectons before this API
        # while using docker compose
        time.sleep(5)

# Writes the measured value
def write_data(temperature, humidity):
    with pg.connect(conn_str) as connection:
        with connection.cursor() as cur:
            timestamp = time.time_ns() // 1000
            cur.execute('INSERT INTO sensor_data VALUES (%s, %s, %s);', (timestamp, temperature, humidity))

# Reads the latest data from the sensor
def read_latest():
    with pg.connect(conn_str) as connection:
        with connection.cursor() as cur:
            cur.execute('SELECT ts, temperature, humidity FROM sensor_data ORDER BY ts DESC LIMIT 1;')
            records = cur.fetchone()

            return {
                'timestamp': records[0],
                'temperature': records[1],
                'humidity': records[2]
            }