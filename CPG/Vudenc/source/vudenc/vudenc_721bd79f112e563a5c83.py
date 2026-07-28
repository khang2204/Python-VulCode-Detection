def __init__(self, connection, args, logger, verb):...
self.connection = connection
self.logger = logger
self.verb = verb
self.path = args.pop()
self.pipe_command = args.pop() if args else None
