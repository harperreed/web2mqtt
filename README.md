# web2mqtt

A Flask-based web service that translates HTTP requests to MQTT messages.

## Features

-   Translates HTTP POST requests to MQTT messages
-   Configurable MQTT broker settings via environment variables
-   Comprehensive logging for easier debugging
-   Docker and docker-compose support for easy deployment

## Setup

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/web2mqtt.git
    cd web2mqtt
    ```

2. (Optional) Create and activate a virtual environment:

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

4. Set up environment variables:
   Create a `.env` file in the project root and add the following variables:
    ```
    MQTT_SERVER=your_mqtt_broker_ip
    MQTT_PORT=1883
    MQTT_KEEPALIVE=60
    FLASK_RUN_PORT=8127
    ```

## Running the Application

### Locally

Run the Flask application:

```
python main.py
```

### Using Docker

Build and run the Docker container:

```
docker-compose up --build
```

## Usage

Send a POST request to translate a message:

```
http://localhost:8127/translate/<topic>/<payload>
```

Replace `<topic>` with your MQTT topic (use '-' instead of '/') and `<payload>` with your message.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
