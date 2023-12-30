# Keyboard-Rumble


This Python script monitors mouse activity using the `pynput` library and sends MQTT messages based on mouse events. It logs mouse movements, button presses/releases, and scroll actions. The script utilizes the `paho.mqtt.client` library to publish messages to an MQTT broker.
The messages are then interpreted by the Pi or Arduino to vibrate the keyboard just like a controller would. 

## Prerequisites

1. Rumble motors 
2. PI or Arduino (to drive the motors) 
3. 3D printed case to attach to the motors to keyboard (optional) 
4. MQTT server

## Schematics
You can use what ever pins you want as long as you can use PWM.


![Rumble Schematics](https://github.com/Slayingripper/Keyboard-Rumble/blob/main/Schematics/keyboard.png)

<video src='https://github.com/Slayingripper/Keyboard-Rumble/blob/main/Schematics/keyboard.mp4' width=180/>

## Usage
Step 1: 

- Desktop.py needs to be running to send data to the server

```
python Desktop.py
```

Step 2: 

```
python rumbler.py
```

## TODO Checklist

- [ ] Add individual mouse click addressing
