def test_parse(self):...
actual = traversal.TraversalPath.parse('level2')
self.assertEqual(traversal.TraversalPath((traversal.NotSupplied, traversal.
    NotSupplied, 'level2')), actual)
actual = traversal.TraversalPath.parse('level2.name')
self.assertEqual(traversal.TraversalPath((traversal.NotSupplied, traversal.
    NotSupplied, 'level2'), (traversal.NotSupplied, traversal.NotSupplied,
    'name')), actual)
actual = traversal.TraversalPath.parse('level2s[b].level3s[1].name')
self.assertEqual(traversal.TraversalPath(('b', traversal.NotSupplied,
    'level2s'), ('1', traversal.NotSupplied, 'level3s'), (traversal.
    NotSupplied, traversal.NotSupplied, 'name')), actual)
actual = traversal.TraversalPath.parse('level2s[b].level3s{code=abc}.name')
self.assertEqual(traversal.TraversalPath(('b', traversal.NotSupplied,
    'level2s'), ('abc', 'code', 'level3s'), (traversal.NotSupplied,
    traversal.NotSupplied, 'name')), actual)
