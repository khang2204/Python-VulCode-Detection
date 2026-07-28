def test_stdio_as(self):...
self.assertTrue(sys.stderr.fileno() > 2,
    'Expected a pseudofile as stderr, got: {}'.format(sys.stderr))
old_stdout, old_stderr, old_stdin = sys.stdout, sys.stderr, sys.stdin
self.assertEqual(sys.stdin.fileno(), 0)
self.assertEqual(sys.stdout.fileno(), 1)
self.assertEqual(sys.stderr.fileno(), 2)
self.assertEqual(sys.stdout, old_stdout)
self.assertEqual(sys.stderr, old_stderr)
self.assertEqual(sys.stdin, old_stdin)
