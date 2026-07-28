def add_subscriber(self, queue):...
"""docstring"""
logger = logging.getLogger(__name__)
logger.debug('Added subscriber')
self.subscribed_queues.append(queue)
