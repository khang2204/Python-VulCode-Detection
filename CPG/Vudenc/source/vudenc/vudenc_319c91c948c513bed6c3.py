def __init__(self, messages_to_wait_for, finished, response):...
self.json_buffer = []
self._logger = logging.getLogger(self.__class__.__name__)
self.messages_to_wait_for = messages_to_wait_for + 1
self.finished = finished
self.response = response
