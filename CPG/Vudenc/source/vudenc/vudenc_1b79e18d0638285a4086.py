def test_test_dir(self):...
test_dir = 'foo'
suite = BokChoyTestSuite('', test_dir=test_dir)
self.assertEqual(suite.cmd, self._expected_command(name=test_dir))
