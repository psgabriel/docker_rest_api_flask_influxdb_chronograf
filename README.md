Package with Influxdb, Chronograf and Phyton Flask

This set is simple to run and can help to build a simple HTTP endpoint to post json documents.
All data will be storage on a Influxdb environment with UI Chronograf.

## Listen ports:
```
0.0.0.0:8888/tcp   chronograf
0.0.0.0:5000/tcp   endpoint
0.0.0.0:8086/tcp   influxdb
````
CHRONOGRAF:
HTTP Access: http://IP:8888/

May be necessary to specify Influxdb connection, so use these informations:
    Connection URL: http://influxdb:8086
    Connection Name: Influx
    Username: test
    Passwdord: test
    Telegraf Database Name: telegraf
    Default Retention Policy: empty

! Skip Kapacitor Connection Setup 

REST API:
HTTP Access: http://IP:5000/postjson
No auth is requiered

Sample data that can be posted:
{
    "measurement": "cpu_load_short",
    "time": "2009-11-11T23:00:00Z",
    "tags": {
        "host": "server02",
        "region": "us-west"
        },
        "fields": {
            "value": 0.65
        }
}