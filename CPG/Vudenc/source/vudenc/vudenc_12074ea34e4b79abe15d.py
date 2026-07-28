def __init__(self, queue):...
"""docstring"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug('Initialized thread')
super(MonitoringThread, self).__init__()
self.job_queue = queue
self.subscribed_queues = []
self.end = False
