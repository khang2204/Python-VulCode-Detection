def test_jinja2_templating(self):...
"""docstring"""
expect = {'SEVERITY': {'HIGH': 4}, 'CONFIDENCE': {'HIGH': 3, 'MEDIUM': 1}}
self.check_example('jinja2_templating.py', expect)
