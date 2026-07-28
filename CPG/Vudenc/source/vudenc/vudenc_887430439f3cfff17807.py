def post_error(self, message):...
"""docstring"""
logging.error('Error: %s\n%s', self._attributes, message)
self.post_event('bot_error', message)
logging.exception('post_error(%s) failed.', message)
