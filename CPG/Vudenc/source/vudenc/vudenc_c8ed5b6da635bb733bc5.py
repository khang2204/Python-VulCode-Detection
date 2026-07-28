def test_prepare_string_argument_sh(self):...
expected_results = ('"normal_string"', '"string with spaces"',
    '"string with quotes\\"a"', '"string with s-quotes\'b"', '"bsn \n A"',
    '"unrecognized \\q escape"')
for string, result in zip(self.test_strings, expected_results):
self.assertEqual(prepare_string_argument(string, 'sh'), result)
