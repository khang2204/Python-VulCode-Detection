def dataReceived(self, data):...
self._logger.info('Received data: %s' % data)
self.json_buffer.append(json.loads(data))
self.messages_to_wait_for -= 1
if self.messages_to_wait_for == 0:
self.response.loseConnection()
