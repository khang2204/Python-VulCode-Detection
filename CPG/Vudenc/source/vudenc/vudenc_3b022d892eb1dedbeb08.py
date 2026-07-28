def test_pickle(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 2, 'MEDIUM': 6}, 'CONFIDENCE': {'HIGH': 8}}
self.check_example('pickle_deserialize.py', expect)
