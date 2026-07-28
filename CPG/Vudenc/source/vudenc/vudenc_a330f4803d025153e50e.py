def test_os_chmod(self):...
"""docstring"""
filename = 'os-chmod-{}.py'
if six.PY2:
filename = filename.format('py2')
filename = filename.format('py3')
expect = {'SEVERITY': {'MEDIUM': 2, 'HIGH': 8}, 'CONFIDENCE': {'MEDIUM': 1,
    'HIGH': 9}}
self.check_example(filename, expect)
