def testUrlOpenPOSTSuccess(self):...
url = 'http://my.url.com'
response = 'True'
url_helper.urllib2.urlopen(url, mox.IgnoreArg(), timeout=mox.IgnoreArg()
    ).AndReturn(StringIO.StringIO(response))
self._mox.ReplayAll()
self.assertEqual(url_helper.UrlOpen(url, method='POST'), response)
self._mox.VerifyAll()
