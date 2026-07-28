def test_find_paths(self):...
paths_small_same_currency = find_paths(expected_graph_small, 'Chaos', 'Chaos')
self.assertListEqual(expected_paths_small_same_currency(),
    paths_small_same_currency)
paths_small_different_currency = find_paths(expected_graph_small.copy(),
    'Chaos', 'Chromatic')
self.assertListEqual(expected_paths_small_different_currency,
    paths_small_different_currency)
