def setUp(self):...
self.loader = RegressionCheckLoader([
    'unittests/resources/checks_unlisted/dependencies/normal.py'])
rt.runtime().resources.prefix = tempfile.mkdtemp(dir='unittests')
