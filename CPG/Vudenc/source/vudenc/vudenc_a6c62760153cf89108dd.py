def test_structure(self):...
TEST_STRUCTURE.full_clean()
resource_iter = TestResourceTraversalIterator(TEST_STRUCTURE)
resources = [('%s %s %s' % (r, r.name, resource_iter.depth)) for r in
    resource_iter]
self.assertListEqual(['on_enter: ', 'on_enter: level2', 'on_exit: level2',
    'on_enter: level2s[a]', 'on_exit: level2s[a]', 'on_enter: level2s[b]',
    'on_enter: level2s[b].level3s[0]', 'on_exit: level2s[b].level3s[0]',
    'on_enter: level2s[b].level3s[1]', 'on_exit: level2s[b].level3s[1]',
    'on_exit: level2s[b]', 'on_enter: level2s[c]',
    'on_enter: level2s[c].level3s[0]', 'on_exit: level2s[c].level3s[0]',
    'on_exit: level2s[c]', 'on_exit: '], resource_iter.events)
self.assertListEqual(['odin.traversal.Level1 resource a 0',
    'odin.traversal.Level2 resource b 1',
    'odin.traversal.Level2 resource c 1',
    'odin.traversal.Level2 resource d 1',
    'odin.traversal.Level3 resource e 2',
    'odin.traversal.Level3 resource f 2',
    'odin.traversal.Level2 resource g 1',
    'odin.traversal.Level3 resource h 2'], resources)
