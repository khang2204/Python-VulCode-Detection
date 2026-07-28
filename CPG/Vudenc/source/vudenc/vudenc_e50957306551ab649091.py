def test_mako_templating(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 3}, 'CONFIDENCE': {'HIGH': 3}}
self.check_example('mako_templating.py', expect)
