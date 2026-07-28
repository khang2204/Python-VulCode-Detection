def setUp(self):...
self._mox = mox.Mox()
self.mock(logging, 'error', lambda *_: None)
self.mock(logging, 'exception', lambda *_: None)
self.mock(logging, 'info', lambda *_: None)
self.mock(logging, 'warning', lambda *_: None)
self._mox.StubOutWithMock(time, 'sleep')
self._mox.StubOutWithMock(urllib2, 'urlopen')
