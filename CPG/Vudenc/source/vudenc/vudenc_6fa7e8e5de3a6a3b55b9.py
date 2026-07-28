import subprocess
def __init__(self, connection, args, logger, verb):...
self.connection = connection
self.logger = logger
self.verb = verb
self.path = args.pop()
self.pipe_command = args.pop() if args else None
def __del__(self):...
self.connection.close()
def run(self, headers={}):...
self.connection.request(self.verb, self.path, headers=headers)
return self.connection.getresponse()
