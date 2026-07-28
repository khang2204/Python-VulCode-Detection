def test_escape_path_argument_unsupported(self):...
_type = 'INVALID'
self.assertEqual(escape_path_argument('/home/usr/a-file', _type),
    '/home/usr/a-file')
self.assertEqual(escape_path_argument('/home/us r/a-file with spaces.bla',
    _type), '/home/us r/a-file with spaces.bla')
self.assertEqual(escape_path_argument('|home|us r|a*dir with spaces|x|',
    _type), '|home|us r|a*dir with spaces|x|')
self.assertEqual(escape_path_argument('system|a|b|c?d', _type),
    'system|a|b|c?d')
