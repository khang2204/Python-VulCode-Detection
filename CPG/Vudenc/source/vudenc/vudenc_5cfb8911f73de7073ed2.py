def __init__(self, command, args):...
self.command = command
self.args = args
self.args.insert(0, command)
self.pid = None
