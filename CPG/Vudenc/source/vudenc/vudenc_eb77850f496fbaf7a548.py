def test_force_local_execution(self):...
self.runner.policy.force_local = True
self.runall([HelloTest()])
stats = self.runner.stats
for t in stats.tasks():
self.assertTrue(t.check.local)
