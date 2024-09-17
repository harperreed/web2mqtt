# 📚 web2mqtt Project README

Welcome to the **web2mqtt** project! This repository provides a lightweight web application that serves as a bridge between a web interface and an MQTT broker. It allows you to send messages via MQTT easily through a REST API.

## 📝 Summary of Project

**web2mqtt** is designed to enable seamless communication between web applications and MQTT brokers. The system uses Flask for web services and paho-mqtt for MQTT messaging. This allows developers to extend IoT capabilities without diving deep into MQTT complexities.

### Key Features:
- 🖥️ Simple REST API for MQTT messaging
- 📦 Dockerized application for easy deployment
- 🌱 Supports environment variable configuration for MQTT settings
- 🔍 Built-in logging for easy debugging and monitoring

## 🚀 How to Use

### Prerequisites:
- Docker and Docker Compose installed on your machine.

### Getting Started:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/harperreed/web2mqtt.git
   cd web2mqtt
   ```

2. **Set environment variables** (Edit `docker-compose.yml`):
   Update the `MQTT_SERVER` and `MQTT_PORT` with your MQTT broker details.

3. **Build and run the Docker container**:
   ```bash
   docker-compose up --build
   ```

4. **Access the API**:
   You can now access the web2mqtt service at `http://localhost:8127`. 

5. **Send a message**:
   To publish a message via the API:
   ```
   GET http://localhost:8127/translate,<topic>,<payload>
   ```
   Replace `<topic>` with the desired topic (e.g., `home/temperature`) and `<payload>` with the message you want to send (e.g., `22`).

### Example:
To publish a temperature message to the home topic:
```
GET http://localhost:8127/translate,home-temperature,22
```

This will replace `-` with `/`, resulting in `home/temperature` as the final MQTT topic.

## 🔧 Tech Info

### Technologies Used:
- **Backend Framework**: [Flask](https://flask.palletsprojects.com/) for handling web requests
- **MQTT Client**: [paho-mqtt](https://www.eclipse.org/paho/) for MQTT communication
- **Environment Management**: [python-dotenv](https://github.com/theskumar/python-dotenv) for loading environment variables
- **Containerization**: [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) for easy deployment and management

### File Structure:
```
web2mqtt/
├── Dockerfile             # Docker configuration for the application
├── docker-compose.yml     # Docker Compose setup
├── main.py                # Core Flask application logic
└── requirements.txt       # Python dependencies
```

Feel free to explore the code, contribute, or reach out if you have any questions! 🚀

Happy Coding! 🖥️✨

---
🔗 GitHub: [harperreed](https://github.com/harperreed)
