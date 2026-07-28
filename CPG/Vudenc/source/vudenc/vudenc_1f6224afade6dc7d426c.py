def load_tests(testclass, name, *args):...
"""docstring"""
if name:
if not name.startswith('test_'):
names = [method for method in dir(testclass) if method.startswith('test_')]
name = 'test_%s' % name
names = [name]
return unittest.TestSuite([testclass(name, *args) for name in names])
