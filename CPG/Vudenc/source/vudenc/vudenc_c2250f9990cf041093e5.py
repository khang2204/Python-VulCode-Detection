def _receive_message(self, msg):...
for i, handler in enumerate(list(self._handlers)):
handle_message, _, _ = handler
self._received.append(msg)
handled = handle_message(msg)
msg, handled = handled
if handled:
self._handlers.remove(handler)
