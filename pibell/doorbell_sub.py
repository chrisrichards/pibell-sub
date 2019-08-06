#!/usr/bin/python

import datetime
import logging
import paho.mqtt.client as mqtt
import pibrella
import threading

def start_alarm():
	pibrella.buzzer.alarm()
	pibrella.light.pulse(0.2)
	thread = threading.Timer(5.0, stop_alarm)
	thread.start()

def stop_alarm():
	pibrella.buzzer.stop()
	pibrella.light.stop()

def on_connect(clinet, userdata, flags, rc):
	logger.info("Connected with result code " + str(rc))
	client.subscribe("home/doorbell/#")

def on_message(client, userdata, msg):
	logger.info(msg.topic + " " + str(msg.payload))
	if (msg.topic == "home/doorbell/state"):
		if (msg.payload == "pressed"):
			logger.info("Pressed")
			start_alarm()
	elif (msg.topic == "home/doorbell/battery"):
		logger.info("Battery: " + msg.payload)

logger = logging.getLogger('doorbell_sub')
logger.setLevel(logging.INFO)

# create file handler
fh = logging.FileHandler('/home/pi/doorbell_sub.log')
fh.setLevel(logging.INFO)

# create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

logger.info("Starting...")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.252")
client.loop_forever()
