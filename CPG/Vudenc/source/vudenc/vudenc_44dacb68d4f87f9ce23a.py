def execute(self, builtins):...
read, write = os.pipe()
inp = RedirectionHelper(0, read)
outp = RedirectionHelper(1, write)
self.first.execute(builtins)
outp.close()
self.second.execute(builtins)
