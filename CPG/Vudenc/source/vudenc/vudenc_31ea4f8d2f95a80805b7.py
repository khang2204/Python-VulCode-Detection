def test_stdin_input(self):...
self.uut.executable = 'more'
self.uut.use_stdin = True
self.uut.use_stderr = False
self.uut.process_output = lambda output, filename, file: output
out = self.uut.lint(file=lines)
self.assertTrue(('abcd\n', 'efgh\n') == out or ('abcd\n', 'efgh\n', '\n') ==
    out)
