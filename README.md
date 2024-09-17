# web2mqtt 🌐 to 📡

Welcome to the **web2mqtt** repository! This project is a Flask-based web service designed to seamlessly translate HTTP requests into MQTT messages. Harnessing the power of MQTT, it opens up vast possibilities for smart homes and IoT applications! 🚀

## Summary of Project 📝

**web2mqtt** allows users to communicate with MQTT brokers using HTTP POST requests directly from a web interface. Whether you're a developer looking to integrate your web services with IoT devices, or simply exploring ways to bridge the HTTP and MQTT protocols, **web2mqtt** is the perfect tool for you! 

## Features 🌟

- Translates HTTP POST requests into MQTT messages 📩
- Configurable MQTT broker settings via environment variables ⚙️
- Comprehensive logging for easier debugging 🐞
- Easy deployment with Docker and docker-compose 🐳

## How to Use 🚀

### Setup 💻

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/harperreed/web2mqtt.git
   cd web2mqtt
   ```

2. **(Optional) Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   
   Create a `.env` file in the project root and add the following variables:

   ```dotenv
   MQTT_SERVER=your_mqtt_broker_ip
   MQTT_PORT=1883
   MQTT_KEEPALIVE=60
   FLASK_RUN_PORT=8127
   ```

### Running the Application 🏃‍♂️

#### Locally

Run the Flask application:

```bash
python main.py
```

#### Using Docker

Build and run the Docker container:

```bash
docker-compose up --build
```

## Usage 💬

Send a POST request to translate a message:

```http
http://localhost:8127/translate/<topic>/<payload>
```

- Replace `<topic>` with your desired MQTT topic (note: use `-` instead of `/`).
- Replace `<payload>` with the message you wish to send.

### Example Request: 

```bash
curl -X POST http://localhost:8127/translate/topic-name/your-message
```

## Tech Info 🛠️

- **Programming Language:** Python 🐍
- **Framework:** Flask 🥳
- **MQTT Library:** Paho MQTT 📡
- **Containerization:** Docker 🐋
- **Environment Variables:** Utilizes `python-dotenv` for managing configurations 🗄️

## Contributing 🤝

Contributions are always welcome! If you have ideas for new features or improvements, feel free to submit a pull request. Please refer to the [contributing guidelines](#) (if available) before making your changes!

---

Thank you for checking out **web2mqtt**! If you have any questions or suggestions, feel free to reach out! 

Happy coding! 🎉
