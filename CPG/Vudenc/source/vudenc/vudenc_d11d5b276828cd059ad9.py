def testUrlOpenPOSTFORMSuccess(self):...
url = 'http://my.url.com'
response = 'True'
url_helper.urllib2.urlopen(mox.IsA(urllib2.Request), timeout=mox.IgnoreArg()
    ).AndReturn(StringIO.StringIO(response))
self._mox.ReplayAll()
self.assertEqual(url_helper.UrlOpen(url, method='POSTFORM'), response)
self._mox.VerifyAll()
