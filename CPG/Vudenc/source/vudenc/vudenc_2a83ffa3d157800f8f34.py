def testEnsureCountKeyIncludedInOpen(self):...
attempts = 5
for i in range(attempts):
encoded_data = urllib.urlencode({url_helper.swarm_constants.COUNT_KEY: i})
self._mox.ReplayAll()
url_helper.urllib2.urlopen(mox.IgnoreArg(), encoded_data, timeout=mox.
    IgnoreArg()).AndRaise(urllib2.URLError('url'))
self.assertEqual(url_helper.UrlOpen('url', max_tries=attempts), None)
if i != attempts - 1:
self._mox.VerifyAll()
time.sleep(mox.IgnoreArg())
