def test_add(self):...
actual = traversal.TraversalPath.parse('level2') + 'name'
self.assertEqual(traversal.TraversalPath.parse('level2.name'), actual)
actual = traversal.TraversalPath.parse('level2s[b]'
    ) + traversal.TraversalPath.parse('level3s[1].name')
self.assertEqual(traversal.TraversalPath.parse('level2s[b].level3s[1].name'
    ), actual)
