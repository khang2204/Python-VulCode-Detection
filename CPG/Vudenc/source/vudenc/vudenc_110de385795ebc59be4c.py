def handler(msg):...
if not match(msg):
return msg, False
event.set()
return msg, True
