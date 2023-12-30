#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// Set your Wi-Fi credentials
const char *ssid = "your-ssid";
const char *password = "your-password";

// Set the GPIO pin for the LEDs
const int mot_pin = D2;    // GPIO2
const int mot2_pin = D1;   // GPIO5

// Set your MQTT broker information
const char *mqtt_server = "ADD_YOUR_SERVER";
const int mqtt_port = 1883;
const char *mqtt_topic = "mouse";

// Initialize the PubSubClient
WiFiClient espClient;
PubSubClient client(espClient);

// Callback when a message is received
void callback(char *topic, byte *payload, unsigned int length) {
  // Check the received message
  if ((char)payload[0] == '1') {
    // Turn on the LEDs
    digitalWrite(mot_pin, HIGH);
    digitalWrite(mot2_pin, HIGH);
    // Delay to keep the LEDs on for a short duration
    delay(200);
    // Turn off the LEDs
    digitalWrite(mot_pin, LOW);
    digitalWrite(mot2_pin, LOW);
  } else if ((char)payload[0] == '0') {
    // Turn off the LEDs
    digitalWrite(mot_pin, LOW);
    digitalWrite(mot2_pin, LOW);
  }
}

void setup() {
  // Setup the LED pins as outputs
  pinMode(mot_pin, OUTPUT);
  pinMode(mot2_pin, OUTPUT);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Setup MQTT client
  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);

  // Connect to the MQTT broker
  while (!client.connected()) {
    if (client.connect("ESP8266Client")) {
      Serial.println("Connected to MQTT");
      client.subscribe(mqtt_topic);
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      Serial.println(" Retrying in 5 seconds...");
      delay(5000);
    }
  }
}

void loop() {
  // Reconnect to the MQTT broker if necessary
  if (!client.connected()) {
    reconnect();
  }

  // Listen for MQTT messages
  client.loop();
}

void reconnect() {
  // Loop until reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("ESP8266Client")) {
      Serial.println("Connected to MQTT");
      // Subscribe to the topic
      client.subscribe(mqtt_topic);
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      Serial.println(" Retrying in 5 seconds...");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
