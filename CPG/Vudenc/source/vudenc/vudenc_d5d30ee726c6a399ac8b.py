def __init__(self, args, log_func):...
self.log_func = log_func
self.args = args
self.mutex = threading.Lock()
self.reload()
