def test_verify_xss(self):...
suite = BokChoyTestSuite('', verify_xss=True)
name = 'tests'
self.assertEqual(suite.cmd, self._expected_command(name=name, verify_xss=True))
