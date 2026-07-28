def test_missing_binary(self):...
old_binary = Lint.executable
invalid_binary = 'invalid_binary_which_doesnt_exist'
Lint.executable = invalid_binary
self.assertEqual(Lint.check_prerequisites(), "'{}' is not installed.".
    format(invalid_binary))
Lint.executable = 'echo'
self.assertTrue(Lint.check_prerequisites())
self.assertTrue(Lint.check_prerequisites())
Lint.executable = old_binary
