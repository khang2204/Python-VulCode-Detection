def test_escape_path_argument_sh(self):...
_type = 'sh'
self.assertEqual(escape_path_argument('/home/usr/a-file', _type),
    '/home/usr/a-file')
self.assertEqual(escape_path_argument('/home/usr/a-dir/', _type),
    '/home/usr/a-dir/')
self.assertEqual(escape_path_argument('/home/us r/a-file with spaces.bla',
    _type), '/home/us\\ r/a-file\\ with\\ spaces.bla')
self.assertEqual(escape_path_argument('/home/us r/a-dir with spaces/x/',
    _type), '/home/us\\ r/a-dir\\ with\\ spaces/x/')
self.assertEqual(escape_path_argument(
    'relative something/with cherries and/pickles.delicious', _type),
    'relative\\ something/with\\ cherries\\ and/pickles.delicious')
