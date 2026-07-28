def __call__(self, msg, arguments, errorSink=None):...
proc = subprocess.Popen(['host', arguments], stdout=subprocess.PIPE)
output, _ = proc.communicate()
output = output.decode().strip()
self.reply(msg, output)
