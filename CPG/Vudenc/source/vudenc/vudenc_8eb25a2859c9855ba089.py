def test_hardcoded_tmp(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 3}, 'CONFIDENCE': {'MEDIUM': 3}}
self.check_example('hardcoded-tmp.py', expect)
