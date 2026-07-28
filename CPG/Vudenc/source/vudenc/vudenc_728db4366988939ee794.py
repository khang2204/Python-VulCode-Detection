def wait(self, timeout=1.0):...
if self._event is None:
return
if not self._event.wait(timeout):
message = 'Timeout waiting for '
if isinstance(self, AwaitableEvent):
message += 'Event {}'.format(self.name)
message += 'Response {}'.format(self.name)
