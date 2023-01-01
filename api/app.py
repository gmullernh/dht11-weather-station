# DHT11
import db
import sensors.dht11 as dht11
import jobs.dht11_job as dht11_job
import pytz

# Add webserver
from flask import Flask
from flask_cors import CORS, cross_origin
import json
from datetime import date, datetime

app = Flask(__name__)
CORS(app)

@app.route('/api/v2', methods=['GET'], defaults={'dataFormat': None})
@app.route('/api/v2/<string:dataFormat>', methods=['GET'])
@cross_origin()
def api_v2(dataFormat):
    r = db.read_latest()

    humidity = r['humidity']
    temperature = r['temperature']

    # Replace with your timezone for conversion
    dttime = (r['timestamp'].replace(tzinfo=pytz.UTC)).astimezone(pytz.timezone('America/Sao_Paulo'))

    contentType = setContentType(dataFormat)

    if humidity != -255 or temperature != -255:
        return formatted_output(humidity, temperature, dttime, contentType), 200, {'Content-Type': contentType}
    else:
        return 'Could not read from DHT11.', 424, {'Content-Type': 'text/plain; charset=utf-8'}

def json_serial(obj):
    '''JSON serializer for objects not serializable by default json code'''

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ('Type %s not serializable' % type(obj))

def setContentType(dataFormat):
    if dataFormat is not None and dataFormat == 'json':
        return 'application/json; charset=utf-8'
    return 'text/plain; charset=utf-8'

def formatted_output(humidity, temperature, date, contentType):
    if contentType == 'application/json; charset=utf-8':
        if date is None:
            date = datetime.now().isoformat() 
        x = { 'temperature' : temperature, 'humidity': humidity, 'datetime': date}
        return json.dumps(x, default=json_serial)
    return '# HELP local_temp local temperature\n# TYPE local_temp gauge\nlocal_temp {}\n# HELP local_humidity local humidity\n# TYPE local_humidity gauge\nlocal_humidity {}\n'.format(temperature, humidity)

if __name__ == '__main__':
    db.init()           # Initialize the database
    dht11.init()        # Initialize the sensor
    dht11_job.init()    # Initialize the job

    print('Initializing webserver')
    app.run(host='0.0.0.0', port=8080) # Intilialize Flask
