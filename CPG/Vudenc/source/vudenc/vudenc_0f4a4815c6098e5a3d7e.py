def _get_message_handle(self, match, handlername):...
event = threading.Event()
def handler(msg):...
if not match(msg):
return msg, False
event.set()
return msg, True
