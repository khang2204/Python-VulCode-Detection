def setUp(self):...
self.loader = RegressionCheckLoader(['unittests/resources/checks'],
    ignore_conflicts=True)
self.runner = executors.Runner(policies.SerialExecutionPolicy())
self.checks = self.loader.load_all()
rt.runtime().resources.prefix = tempfile.mkdtemp(dir='unittests')
rt.runtime()._current_run = 0
