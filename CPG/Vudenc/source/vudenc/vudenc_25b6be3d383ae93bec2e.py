def testUrlOpenInvalidWaitDuration(self):...
self._mox.ReplayAll()
self.assertEqual(url_helper.UrlOpen('url', wait_duration=-1), None)
self._mox.VerifyAll()
