def testUrlOpenHTTPErrorWithRetry(self):...
response = 'response'
url_helper.urllib2.urlopen(mox.IgnoreArg(), mox.IgnoreArg(), timeout=mox.
    IgnoreArg()).AndRaise(urllib2.HTTPError('url', 500, 'error message',
    None, None))
time.sleep(mox.IgnoreArg())
url_helper.urllib2.urlopen(mox.IgnoreArg(), mox.IgnoreArg(), timeout=mox.
    IgnoreArg()).AndReturn(StringIO.StringIO(response))
self._mox.ReplayAll()
self.assertEqual(response, url_helper.UrlOpen('url', max_tries=10))
self._mox.VerifyAll()
