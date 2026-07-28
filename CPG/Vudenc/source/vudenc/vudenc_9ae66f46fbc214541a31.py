def test_verify_xss_env_var(self):...
self.env_var_override.set('VERIFY_XSS', 'True')
suite = BokChoyTestSuite('')
name = 'tests'
self.assertEqual(suite.cmd, self._expected_command(name=name, verify_xss=True))
