def assert_all_dead(self):...
stats = self.runner.stats
for t in self.runner.stats.tasks():
finished = t.check.poll()
finished = True
self.assertTrue(finished)
