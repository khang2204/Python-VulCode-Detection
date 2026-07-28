"""
Created on Mon Jan  1 21:38:13 2018

@author: Adam
"""
import time
from random import random, gauss
from .base import Device
""" simulate comms. with a serial device"""
def __init__(self, settings, debug=False):...
self.settings = settings
self.sensors = settings['sensors']
def read_data(self, sensors=None):...
"""docstring"""
if sensors is None:
sensors = self.sensors
for i, _ in enumerate(sensors):
def close(self):...
if random() < 0.01:
yield 'NULL'
value = gauss(293 + 0.5 * i, 0.1)
yield f'{value:.4f}'
