def test_escape_path_argument_cmd(self):...
_type = 'cmd'
self.assertEqual(escape_path_argument('C:\\Windows\\has-a-weird-shell.txt',
    _type), '"C:\\Windows\\has-a-weird-shell.txt"')
self.assertEqual(escape_path_argument('C:\\Windows\\lolrofl\\dirs\\', _type
    ), '"C:\\Windows\\lolrofl\\dirs\\"')
self.assertEqual(escape_path_argument('X:\\Users\\Maito Gai\\fi le.exe',
    _type), '"X:\\Users\\Maito Gai\\fi le.exe"')
self.assertEqual(escape_path_argument('X:\\Users\\Mai to Gai\\director y\\',
    _type), '"X:\\Users\\Mai to Gai\\director y\\"')
self.assertEqual(escape_path_argument(
    'X:\\Users\\Maito Gai\\"seven-gates".y', _type),
    '"X:\\Users\\Maito Gai\\^"seven-gates^".y"')
self.assertEqual(escape_path_argument('System32\\my-custom relative tool\\',
    _type), '"System32\\my-custom relative tool\\"')
self.assertEqual(escape_path_argument('System32\\illegal" name "".curd',
    _type), '"System32\\illegal^" name ^"^".curd"')
