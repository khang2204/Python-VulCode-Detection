def setUp(self):...
super(TestCase, self).setUp()
self.mock(net, 'url_open', self._url_open)
self.mock(net, 'url_read_json', self._url_read_json)
self.mock(net, 'sleep_before_retry', lambda *_: None)
self._lock = threading.Lock()
self._requests = []
