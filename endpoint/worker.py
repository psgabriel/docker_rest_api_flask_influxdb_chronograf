from flask import Flask
from flask import request

from influxdb import InfluxDBClient
import json

# Influxdb Connection
host = 'influxdb'
port = 8086
user = 'test'
password = 'test'
db_name = 'influx'

influx = InfluxDBClient(host, port, user, password)

app = Flask(__name__)
@app.route('/postjson', methods=['POST'])
def postJsonHandler():
    #print(request.is_json)
    content = request.get_json()

    dictlist = []
    dictlist.append(content)

    db_list = influx.get_list_database()
    #print(influx.get_list_database())
    if db_name not in [str(x['name']) for x in db_list]:
        influx.create_database(db_name)
    else:
        influx.switch_database(db_name)

    influx.write_points(dictlist)
    return 'data posted'


app.run(host='0.0.0.0', port=5000)