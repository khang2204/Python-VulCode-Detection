def test_invalid_default_store(self):...
suite = BokChoyTestSuite('', default_store='invalid')
name = 'tests'
self.assertEqual(suite.cmd, self._expected_command(name=name, store='invalid'))
