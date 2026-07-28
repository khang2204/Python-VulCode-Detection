def testUrlOpenInvalidTryCount(self):...
self._mox.ReplayAll()
self.assertEqual(url_helper.UrlOpen('url', max_tries=-1), None)
self._mox.VerifyAll()
