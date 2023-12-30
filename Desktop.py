from pynput.mouse import Listener
import logging
import paho.mqtt.client as mqtt

# Set up MQTT parameters
mqtt_broker_address = "ADD YOUR SERVER"
mqtt_topic = "mouse"

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse button pressed at ({0}, {1}) with {2}'.format(x, y, button))
        send_mqtt_message('1')  # Button is pressed, send 1
    else:
        logging.info('Mouse button released at ({0}, {1}) with {2}'.format(x, y, button))
        send_mqtt_message('0')  # Button is released, send 0

def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
    send_mqtt_message('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

def send_mqtt_message(message):
    client = mqtt.Client()
    client.connect(mqtt_broker_address, 1883, 60)
    client.publish(mqtt_topic, message)
    client.disconnect()

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
