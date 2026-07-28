def test_spec_with_draft_default_store(self):...
spec = 'test_foo.py'
suite = BokChoyTestSuite('', test_spec=spec, default_store='draft')
name = 'tests/{}'.format(spec)
self.assertEqual(suite.cmd, self._expected_command(name=name, store='draft'))
