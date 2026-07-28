def __init__(self, worker):...
self.worker = worker
self.events = []
self.lock = threading.Lock()
