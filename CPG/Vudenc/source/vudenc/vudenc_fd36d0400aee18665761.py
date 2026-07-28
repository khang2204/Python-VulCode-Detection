def test_build_conversions(self):...
path = expected_paths_small_same_currency()[0]
conversion = build_conversion(path)
print(conversion)
self.assertDictEqual(expected_conversion, conversion)
