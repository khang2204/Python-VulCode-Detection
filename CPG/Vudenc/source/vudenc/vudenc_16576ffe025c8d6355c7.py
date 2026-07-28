def test_eval(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 3}, 'CONFIDENCE': {'HIGH': 3}}
self.check_example('eval.py', expect)
