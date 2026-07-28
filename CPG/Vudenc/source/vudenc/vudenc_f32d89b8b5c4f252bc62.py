def testNonAcsiiData(self):...
data = {'r': u'not ascii £ һ'}
url = 'http://my.url.com'
response = 'True'
url_helper.urllib2.urlopen(mox.StrContains(url), mox.IgnoreArg(), timeout=
    mox.IgnoreArg()).AndReturn(StringIO.StringIO(response))
self._mox.ReplayAll()
self.assertEqual(url_helper.UrlOpen(url, data=data), response)
self._mox.VerifyAll()
