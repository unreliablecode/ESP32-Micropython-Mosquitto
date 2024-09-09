import network
import time
from umqtt.simple import MQTTClient

SSID = 'Wokwi-GUEST'
PASSWORD = ''

MQTT_SERVER = 'your hostname'  # IP or domain of your VPS
MQTT_PORT = 1883
MQTT_TOPIC_PUB = b'test/topic'
MQTT_TOPIC_SUB = b'test/response'

def connect_to_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    if not wifi.isconnected():
        print('Connecting to network...')
        wifi.connect(SSID, PASSWORD)
        while not wifi.isconnected():
            pass
    print('Network config:', wifi.ifconfig())

def mqtt_callback(topic, msg):
    print('Received message:', msg)

def main():
    connect_to_wifi()
    
    # Connect to MQTT server
    client = MQTTClient('esp_client', MQTT_SERVER, port=MQTT_PORT)
    client.set_callback(mqtt_callback)
    client.connect()
    
    client.subscribe(MQTT_TOPIC_SUB)
    
    print('Connected to MQTT server and subscribed to topic.')
    
    try:
        while True:
            # Check for new messages
            client.check_msg()

            # Publish a message
            client.publish(MQTT_TOPIC_PUB, b'Hello from ESP')
            print('Message sent to', MQTT_TOPIC_PUB)

            time.sleep(5)  # Wait before sending the next message
    except KeyboardInterrupt:
        print('Disconnecting...')
        client.disconnect()

if __name__ == '__main__':
    main()
