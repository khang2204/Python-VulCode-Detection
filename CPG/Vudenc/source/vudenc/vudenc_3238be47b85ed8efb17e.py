def setUp(self):...
super(UrlHelperTest, self).setUp()
self.mock(logging, 'error', lambda *_: None)
self.mock(logging, 'exception', lambda *_: None)
self.mock(logging, 'info', lambda *_: None)
self.mock(logging, 'warning', lambda *_: None)
self.mock(time, 'sleep', lambda _: None)
