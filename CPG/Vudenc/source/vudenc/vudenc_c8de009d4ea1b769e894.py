def setUp(self):...
super(TestPaverPa11yCrawlerCmd, self).setUp()
mock_sh = patch('pavelib.utils.test.suites.bokchoy_suite.sh')
self._mock_sh = mock_sh.start()
self.addCleanup(mock_sh.stop)
