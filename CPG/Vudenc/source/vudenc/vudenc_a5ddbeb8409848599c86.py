def testUrlOpenSuccessAfterFailure(self):...
url_helper.urllib2.urlopen(mox.IgnoreArg(), mox.IgnoreArg(), timeout=mox.
    IgnoreArg()).AndRaise(urllib2.URLError('url'))
time.sleep(mox.IgnoreArg())
response = 'True'
url_helper.urllib2.urlopen(mox.IgnoreArg(), mox.IgnoreArg(), timeout=mox.
    IgnoreArg()).AndReturn(StringIO.StringIO(response))
self._mox.ReplayAll()
self.assertEqual(url_helper.UrlOpen('url', max_tries=2), response)
self._mox.VerifyAll()
