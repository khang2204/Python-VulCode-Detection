def execute(self, builtins):...
if self.command in builtins:
builtins[self.command](*self.args)
pid = os.fork()
if pid == 0:
os.execv(self.full_command, self.args)
self.pid = pid
