import os
from flask import Flask
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

# MQTT configuration
MQTT_SERVER = os.getenv('MQTT_SERVER', '192.168.200.8')
MQTT_PORT = int(os.getenv('MQTT_PORT', 1883))
MQTT_KEEPALIVE = int(os.getenv('MQTT_KEEPALIVE', 60))

def publish_message(topic: str, payload: str) -> None:
    """Publish a message to the MQTT broker."""
    try:
        publish.single(
            topic,
            payload=payload,
            qos=0,
            retain=True,
            hostname=MQTT_SERVER,
            port=MQTT_PORT,
            keepalive=MQTT_KEEPALIVE,
            protocol=mqtt.MQTTv311
        )
        logger.info(f"Message published - Topic: {topic}, Payload: {payload}")
    except Exception as e:
        logger.error(f"Failed to publish message - Topic: {topic}, Payload: {payload}, Error: {str(e)}")
        raise

@app.route('/translate,<topic>,<payload>')
def translate(topic: str, payload: str):
    """Handle translation requests."""
    logger.debug(f"Received translation request - Topic: {topic}, Payload: {payload}")
    
    try:
        # Replace '-' with '/' in the topic
        formatted_topic = topic.replace('-', '/')
        
        publish_message(formatted_topic, payload)
        
        return 'OK', 200
    except Exception as e:
        logger.error(f"Error in translate route: {str(e)}")
        return str(e), 500

@app.route('/')
def hello():
    """Root route for basic health check."""
    logger.debug("Root route accessed")
    return 'web2mqtt', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('FLASK_RUN_PORT', 8127)), debug=True)
