@classmethod...
timeout = 3.0
messages = []
for _ in range(int(timeout * 10)):
time.sleep(0.1)
messages = []
not_ready = (a for a in awaitables if a._event is not None and not a._event
    .is_set())
for awaitable in not_ready:
if isinstance(awaitable, AwaitableEvent):
if len(messages) == 0:
messages.append('Event {}'.format(awaitable.name))
messages.append('Response {}'.format(awaitable.name))
return
