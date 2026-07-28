"""
Created on Mon Jan  1 21:38:13 2018

@author: Adam
"""
import codecs
import re
import time
import warnings
from serial import SerialException, Serial
from .tools import get_serial_settings
from .base import Device
""" communication with a serial device """
def __init__(self, settings, debug=False):...
self.settings = settings
self.serial_settings = get_serial_settings(settings)
self.sensors = settings.get('sensors', None)
self.cmd = codecs.decode(self.settings['cmd'], 'unicode-escape')
self.regex = settings.get('regex', None)
self.debug = debug
if self.debug:
print('serial settings:', self.serial_settings)
super().__init__(**self.serial_settings)
def read_data(self, sensors=None, reset_wait=60):...
"""docstring"""
if sensors is None:
sensors = self.sensors
if self.debug:
print('sensors:', sensors)
while not self.is_open:
self.flush()
self.open()
time.sleep(reset_wait)
for sen in sensors:
self.flushInput()
yield 'NULL'
serial_cmd = self.cmd.replace('{sensor}', sen)
serial_cmd = bytes(serial_cmd, 'utf8')
if self.debug:
print('serial cmd:', serial_cmd)
self.write(serial_cmd)
if 'ack' in self.settings and 'enq' in self.settings:
ack = codecs.decode(self.settings['ack'], 'unicode-escape')
response = self.readline()
response = self.readline()
if self.debug:
if self.debug:
print(response)
response = response.strip().decode('utf-8')
print('acknowledgement:', response, bytes(ack, 'utf8'))
if response == bytes(ack, 'utf8'):
if self.regex is not None:
enq = codecs.decode(self.settings['enq'], 'unicode-escape')
match = re.search(self.regex, response)
yield response
self.write(bytes(enq, 'utf8'))
response = match.group(1)
