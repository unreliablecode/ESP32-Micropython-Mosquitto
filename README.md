# MicroPython MQTT Client for ESP32/ESP8266

This project demonstrates how to set up an MQTT client using MicroPython on ESP32/ESP8266 devices. The ESP device connects to an open WiFi network and communicates with a Mosquitto MQTT broker hosted on a cloud VPS.

## Features

- Connects to an open WiFi network (e.g., "Wokwi-GUEST").
- Publishes and subscribes to MQTT topics.
- Supports connection to a Mosquitto MQTT broker running on a VPS or local server.

## Prerequisites

- ESP32 or ESP8266 with MicroPython firmware.
- A Mosquitto MQTT broker hosted on a VPS (or locally).
- Open WiFi network (e.g., "Wokwi-GUEST").

## Getting Started

### 1. Flash MicroPython Firmware

Ensure you have MicroPython firmware installed on your ESP32/ESP8266. You can use tools like `esptool.py` to flash MicroPython onto your device.

### 2. Clone or Download the Repository

```bash
git clone https://github.com/your-username/esp-micropython-mqtt.git
cd esp-micropython-mqtt
```

### 3. Setup MQTT Broker (Cloud VPS)

You can set up an MQTT broker using [Mosquitto](https://mosquitto.org/) on a VPS or locally. Here’s a quick setup guide for a VPS:

1. SSH into your VPS and install Mosquitto:
   ```bash
   sudo apt update
   sudo apt install mosquitto mosquitto-clients
   ```

2. Configure Mosquitto to allow external connections:
   ```bash
   sudo nano /etc/mosquitto/mosquitto.conf
   ```

   Add the following lines:
   ```conf
   listener 1883 0.0.0.0
   allow_anonymous true
   ```

3. Restart the Mosquitto service:
   ```bash
   sudo systemctl restart mosquitto
   ```

4. Ensure port 1883 is open on the firewall:
   ```bash
   sudo ufw allow 1883
   ```

### 4. Setup ESP32/ESP8266

Upload the `main.py` file to your ESP32/ESP8266 using `ampy`, `rshell`, or the `Thonny` IDE.

### 5. MicroPython Code (`main.py`)

The `main.py` script connects your ESP device to the open WiFi network "Wokwi-GUEST" and sets up MQTT communication with the broker. 

### 6. Test the MQTT Connection

You can use the `mosquitto_sub` client to subscribe to the MQTT topics and see the messages sent by the ESP device:

```bash
mosquitto_sub -h your-server-ip -t test/topic
```

### 7. Customize the Code

You can customize the topics or add more functionality to the script as needed. For example, you could use sensors connected to the ESP to publish sensor readings to the MQTT broker.

## Troubleshooting

- **ESP not connecting to WiFi:** Ensure that the SSID is correct, and the network is open (no password).
- **MQTT broker not reachable:** Verify that port 1883 is open on the VPS and the IP address is correct.

### Key Sections:
1. **Project Description** – Describes the project and the technology used.
2. **Prerequisites** – Details the hardware and software needed.
3. **Setup Instructions** – Step-by-step guide for setting up the MQTT broker and ESP32/ESP8266.
4. **MicroPython Code** – Provides the MicroPython script for communication.
5. **Testing** – Explains how to test the connection and see the results.
6. **Troubleshooting** – Offers basic debugging tips.

You can modify the GitHub URL in the **Clone or Download** section to match your repository link.
