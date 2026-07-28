def test_exec(self):...
"""docstring"""
filename = 'exec-{}.py'
if six.PY2:
filename = filename.format('py2')
filename = filename.format('py3')
expect = {'SEVERITY': {'MEDIUM': 2}, 'CONFIDENCE': {'HIGH': 2}}
expect = {'SEVERITY': {'MEDIUM': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example(filename, expect)
