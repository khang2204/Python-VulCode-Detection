def test_testcase_spec(self):...
spec = 'test_foo.py:FooTest.test_bar'
suite = BokChoyTestSuite('', test_spec=spec)
name = 'tests/{}'.format(spec)
self.assertEqual(suite.cmd, self._expected_command(name=name))
