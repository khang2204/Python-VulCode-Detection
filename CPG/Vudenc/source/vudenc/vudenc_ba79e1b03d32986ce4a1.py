def __init__(self, worker, mode):...
self.worker = worker
self.mode = mode
self.redis_client = worker.redis_client
