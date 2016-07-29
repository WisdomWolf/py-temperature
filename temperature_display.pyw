#!/usr/bin/env python

import sys
import time
import Adafruit_MCP9808.MCP9808 as MCP9808

from Adafruit_IO import MQTTClient

ADAFRUIT_IO_KEY = 'aad2a690116830b5c78c86426ed35b76212ae3d7'
ADAFRUIT_IO_USERNAME = 'WisdomWolf'

sensor = MCP9808.MCP9808()
sensor.begin()


def connected(client):
    print('Connected to Adafruit IO!')


def disconnected(client):
    print('Disconnected from Adafruit IO!')


def message(client, feed_id, payload):
    print('Feed {0} received new value: {1}'.format(feed_id, payload))

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message

client.connect()

client.loop_background()


def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0

print('Press Ctrl-C to quit.')
while True:
    temp = sensor.readTempC()
    farenheit = c_to_f(temp)
    sys.stdout.write('\rTemperature: {:0.3F}*F'.format(farenheit))
    sys.stdout.flush()
    client.publish('Temperature_Work', farenheit)
    time.sleep(1.0)
