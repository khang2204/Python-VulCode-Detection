def test_get_dimensions(self):...
dimensions = set(bot_main.get_dimensions(None))
dimensions.discard('hidpi')
dimensions.discard('zone')
expected = {'cores', 'cpu', 'gpu', 'id', 'machine_type', 'os', 'pool'}
self.assertEqual(expected, dimensions)
