def handler(msg):...
if not match(msg):
return msg, False
lock.release()
return msg, True
