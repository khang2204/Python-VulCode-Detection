def __call__(self, msg, arguments, errorSink=None):...
if arguments.strip():
return
self.xmpp.config.reload()
