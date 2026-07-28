def __call__(self, msg, arguments, errorSink=None):...
if arguments.strip():
return
proc = subprocess.Popen(['uptime'], stdout=subprocess.PIPE)
output, _ = proc.communicate()
output = output.decode().strip()
if not self._show_users:
output = re.sub('[0-9]+ users, ', '', output)
self.reply(msg, output)
