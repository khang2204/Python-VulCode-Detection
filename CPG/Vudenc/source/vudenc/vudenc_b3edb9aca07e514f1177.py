def test_invalid_path(self):...
path = traversal.TraversalPath.parse('level2s[b].level3s[4]')
self.assertRaises(IndexError, path.get_value, TEST_STRUCTURE)
path = traversal.TraversalPath.parse('level2s[b].level3s_sd[1]')
self.assertRaises(KeyError, path.get_value, TEST_STRUCTURE)
