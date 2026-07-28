def execute(self, *args):...
self.first.execute(*args)
self.first.wait()
self.second.execute(*args)
self.second.wait()
