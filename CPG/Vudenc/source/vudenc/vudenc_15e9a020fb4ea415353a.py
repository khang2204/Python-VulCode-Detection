def testCountKeyInData(self):...
data = {url_helper.swarm_constants.COUNT_KEY: 1}
self._mox.ReplayAll()
self.assertEqual(url_helper.UrlOpen('url', data=data), None)
self._mox.VerifyAll()
