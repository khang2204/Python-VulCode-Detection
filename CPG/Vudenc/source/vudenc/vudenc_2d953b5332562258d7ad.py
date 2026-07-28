def testUrlOpenHTTPErrorNoRetry(self):...
url_helper.urllib2.urlopen(mox.IgnoreArg(), mox.IgnoreArg(), timeout=mox.
    IgnoreArg()).AndRaise(urllib2.HTTPError('url', 400, 'error message',
    None, None))
self._mox.ReplayAll()
self.assertIsNone(url_helper.UrlOpen('url', max_tries=10))
self._mox.VerifyAll()
