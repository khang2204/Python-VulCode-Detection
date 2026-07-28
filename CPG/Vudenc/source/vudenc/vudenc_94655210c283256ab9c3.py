def test_suite_spec(self):...
spec = 'test_foo.py'
suite = BokChoyTestSuite('', test_spec=spec)
name = 'tests/{}'.format(spec)
self.assertEqual(suite.cmd, self._expected_command(name=name))
