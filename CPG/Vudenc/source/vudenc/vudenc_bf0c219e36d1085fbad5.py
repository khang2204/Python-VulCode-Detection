def testUrlOpenGETSuccess(self):...
url = 'http://my.url.com'
response = 'True'
url_helper.urllib2.urlopen(mox.StrContains(url), timeout=mox.IgnoreArg()
    ).AndReturn(StringIO.StringIO(response))
self._mox.ReplayAll()
self.assertEqual(url_helper.UrlOpen(url, method='GET'), response)
self._mox.VerifyAll()
