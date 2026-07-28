def test_poll_fails_busy_loop(self):...
num_tasks = 3
checks = [SleepCheckPollFailLate(1 / i) for i in range(1, num_tasks + 1)]
num_checks = len(checks)
self.set_max_jobs(1)
self.runall(checks)
stats = self.runner.stats
self.assertEqual(num_tasks, stats.num_cases())
self.assertEqual(num_tasks, len(stats.failures()))
