# ESP8266 MQTT Control with LEDs

This Arduino sketch demonstrates how to control LEDs connected to GPIO pins on an ESP8266 microcontroller using MQTT messages. The ESP8266 connects to a Wi-Fi network, subscribes to a specific MQTT topic, and reacts to incoming messages to turn on or off the connected LEDs.

## Prerequisites

Before uploading this sketch to your ESP8266, ensure that you have the following:

- Arduino IDE installed on your computer.
- The necessary libraries installed:
  - `ESP8266WiFi` for Wi-Fi connectivity.
  - `PubSubClient` for MQTT communication.

## Configuration

1. Open the sketch in the Arduino IDE.
2. Update the Wi-Fi credentials (`ssid` and `password`) to match your network.
3. Set the GPIO pin numbers for the LEDs (`mot_pin` and `mot2_pin`).
4. Update the MQTT broker information (`mqtt_server`, `mqtt_port`, and `mqtt_topic`).

## How It Works

1. The ESP8266 connects to the specified Wi-Fi network.
2. It establishes a connection to the MQTT broker using the `PubSubClient` library.
3. The microcontroller subscribes to the specified MQTT topic (`mqtt_topic`).
4. Upon receiving MQTT messages on the subscribed topic, the ESP8266 interprets the message payload.
5. If the payload is '1', it turns on the LEDs for a short duration and then turns them off.
6. If the payload is '0', it turns off the LEDs.

## Uploading the Sketch

1. Connect your ESP8266 to your computer.
2. Select the correct board and port in the Arduino IDE.
3. Upload the sketch to the ESP8266.

## Serial Monitor

To monitor the ESP8266's status and debug messages, open the Serial Monitor in the Arduino IDE.

## Troubleshooting

- If the LEDs don't respond to MQTT messages, check the Wi-Fi credentials and MQTT broker settings.
- Ensure that the required libraries are installed in the Arduino IDE.

