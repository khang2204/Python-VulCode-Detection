def test_concurrency_unlimited(self):...
checks = [SleepCheck(0.5) for i in range(3)]
self.set_max_jobs(len(checks))
self.runall(checks)
self.assertEqual(len(checks), self.runner.stats.num_cases())
self.assertEqual(0, len(self.runner.stats.failures()))
self.assertEqual(len(checks), max(self.monitor.num_tasks))
self.assertEqual(len(checks), self.monitor.num_tasks[len(checks)])
self.read_timestamps(self.monitor.tasks)
if self.begin_stamps[-1] > self.end_stamps[0]:
self.skipTest('the system seems too much loaded.')
