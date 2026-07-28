def test_nonsense(self):...
"""docstring"""
self.run_example('nonsense.py')
self.assertEqual(1, len(self.b_mgr.skipped))
