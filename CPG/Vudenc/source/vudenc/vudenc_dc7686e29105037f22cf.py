def test_valid_path(self):...
self.assertEqual('a', traversal.TraversalPath.parse('name').get_value(
    TEST_STRUCTURE))
self.assertEqual('b', traversal.TraversalPath.parse('level2.name').
    get_value(TEST_STRUCTURE))
r = traversal.TraversalPath.parse('level2s[b].level3s[1]').get_value(
    TEST_STRUCTURE)
self.assertIsInstance(r, Level3)
self.assertEqual('f', r.name)
