def kill(self):...
"""docstring"""
logger = logging.getLogger(__name__)
logger.debug('Killing process monitoring thread')
self.end = True
