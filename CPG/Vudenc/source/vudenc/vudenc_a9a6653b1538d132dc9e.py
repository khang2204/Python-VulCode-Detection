def test_default(self):...
suite = BokChoyTestSuite('')
name = 'tests'
self.assertEqual(suite.cmd, self._expected_command(name=name))
