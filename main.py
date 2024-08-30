from flask import Flask, request
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/translate,<topic>,<payload>')
def translate(topic, payload):
    
    topic = topic.replace('-', '/')

    mqtt_server = "192.168.200.8"
    publish.single(topic, payload=payload, qos=0, retain=True, hostname=mqtt_server, port=1883,keepalive=60, protocol=mqtt.MQTTv311, transport="tcp")

    return 'OK'

@app.route('/')
def hello():
    return 'web2mqtt'
