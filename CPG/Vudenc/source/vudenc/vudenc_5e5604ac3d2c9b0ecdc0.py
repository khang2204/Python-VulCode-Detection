def __call__(self, msg, arguments, errorSink=None):...
if len(arguments.strip()) > 0:
return
self.reply(msg, random.choice(self.fnordlist))
return True
