def testUrlOpenFailure(self):...
url_helper.urllib2.urlopen(mox.IgnoreArg(), mox.IgnoreArg(), timeout=mox.
    IgnoreArg()).AndRaise(urllib2.URLError('url'))
self._mox.ReplayAll()
self.assertIsNone(url_helper.UrlOpen('url', max_tries=1))
self._mox.VerifyAll()
