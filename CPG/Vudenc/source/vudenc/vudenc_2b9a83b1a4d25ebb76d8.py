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
