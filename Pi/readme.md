# Raspberry Pi GPIO Control with MQTT

This Python script is designed to run on a Raspberry Pi (RPi) and control LEDs connected to GPIO pins using MQTT messages. The script utilizes the RPi.GPIO library for GPIO control and the paho.mqtt.client library for MQTT communication.

## Prerequisites

- Raspberry Pi with RPi.GPIO library installed.
- MQTT broker running (Update `mqtt_broker` in the script with your broker's IP address).

## Configuration

1. Install the required Python libraries:
   ```
   pip install RPi.GPIO paho-mqtt
   ```
   
2. Update script variables:

    Set GPIO pin numbers (mot_pin and mot2_pin) for the Motors.
    
    Update MQTT broker information (mqtt_broker, mqtt_port, and mqtt_topic).
    
## Usage

    Run the script on your Raspberry Pi:
```
python script_name.py
```
The script will connect to the MQTT broker and listen for messages on the specified topic. The Motors will respond based on received messages.

## Notes
    Press Ctrl+C to exit the script gracefully.
