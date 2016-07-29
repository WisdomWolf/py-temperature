#!/usr/bin/env python

import sys
import time
import Adafruit_MCP9808.MCP9808 as MCP9808

sensor = MCP9808.MCP9808()
sensor.begin()

def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0

print('Press Ctrl-C to quit.')
while True:
    temp = sensor.readTempC()
    sys.stdout.write('\rTemperature: {:0.3F}*F'.format(c_to_f(temp)))
    sys.stdout.flush()
    time.sleep(1.0)
