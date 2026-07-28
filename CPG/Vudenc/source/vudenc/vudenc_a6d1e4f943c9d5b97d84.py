def test_poll_fails_main_loop(self):...
num_tasks = 3
checks = [SleepCheckPollFail(10) for i in range(num_tasks)]
num_checks = len(checks)
self.set_max_jobs(1)
self.runall(checks)
stats = self.runner.stats
self.assertEqual(num_tasks, stats.num_cases())
self.assertEqual(num_tasks, len(stats.failures()))
