def test_stderr_output(self):...
self.uut.executable = 'echo'
self.uut.arguments = 'hello'
self.uut.use_stdin = False
self.uut.use_stderr = True
self.uut.process_output = lambda output, filename, file: output
out = self.uut.lint('unused_filename')
self.assertEqual((), out)
self.uut.use_stderr = False
out = self.uut.lint('unused_filename')
self.assertEqual(('hello\n',), out)
def assert_warn(line):...
assert line == 'hello'
old_warn = self.uut.warn
self.uut.warn = assert_warn
self.uut._print_errors(['hello', '\n'])
self.uut.warn = old_warn
