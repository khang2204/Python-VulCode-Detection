def test_mark_safe(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example('mark_safe.py', expect)
