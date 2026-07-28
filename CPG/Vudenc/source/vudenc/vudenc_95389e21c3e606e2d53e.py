def test_stdio_as_dev_null(self):...
self.assertEqual('', sys.stdin.read())
print('garbage', file=sys.stdout)
print('garbage', file=sys.stderr)
