def __init__(self, log_dir=None):...
self.total = 0
self.success = 0
self.failure = 0
self.error = 0
self.undecided = 0
self.total_time = 0.0
self.max_time = 0.0
self.log_dir = log_dir
if self.log_dir is not None:
os.makedirs(self.log_dir)
