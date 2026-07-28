def test_get_prefixed_value(self):...
lines = ['Line1 passed', 'Line1 failed']
prefix = ['Line1', 'Line2']
expected_output = [' passed', None]
self.assertEqual(self.driver._get_prefixed_value(lines, prefix[0]),
    expected_output[0])
self.assertEqual(self.driver._get_prefixed_value(lines, prefix[1]),
    expected_output[1])
