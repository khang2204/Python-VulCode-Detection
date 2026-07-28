def __call__(self, msg, arguments, errorSink=None):...
if self.variableTo:
if msg['type'] == 'groupchat':
to, mtype, body = arguments.split(' ', 2)
self.reply(msg, body, overrideTo=to, overrideMType=mtype)
to = msg['from'].bare
to = msg['from']
body = arguments
mtype = None
