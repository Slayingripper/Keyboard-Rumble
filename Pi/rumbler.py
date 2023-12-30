import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin for the LED
mot_pin = 2
mot2_pin = 26
# Set your MQTT broker information
mqtt_broker = "ADD_YOUR_MQTT_SERVER"
mqtt_port = 1883
mqtt_topic = "mouse"

# Setup the LED pin as an output
GPIO.setup(mot_pin, GPIO.OUT)
GPIO.setup(mot2_pin,GPIO.OUT)

# Callback when a message is received
def on_message(client, userdata, msg):
    #print("Received message on topic: " + msg.topic)
    
    # Check the received message
    if msg.payload.decode("utf-8") == '1':
        # Turn on toutpuithe LED
        GPIO.output(mot_pin, GPIO.HIGH)
        GPIO.output(mot2_pin,GPIO.HIGH)
        #print("LED ON")
        #time.sleep(0.2)  # Keep the LED on for 0.2 seconds

        # Turn off the LED
        #GPIO.output(led_pin, GPIO.LOW)
        #print("LED OFF")
    elif msg.payload.decode("utf-8") == '0':
        # Turn off the LED
        GPIO.output(mot_pin, GPIO.LOW)
        GPIO.output(mot2_pin,GPIO.LOW)
        #print("LED OFF")

# Setup MQTT client
client = mqtt.Client()
client.on_message = on_message

# Connect to the MQTT broker
client.connect(mqtt_broker, mqtt_port, 60)
client.subscribe(mqtt_topic)

try:
    # Loop to listen for MQTT messages
    client.loop_forever()

except KeyboardInterrupt:
    print("Ctrl+C pressed. Exiting...")

finally:
    # Cleanup GPIO on exit
    GPIO.cleanup()

