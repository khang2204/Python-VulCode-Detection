def test_concurrency_none(self):...
checks = [SleepCheck(0.5) for i in range(3)]
num_checks = len(checks)
self.set_max_jobs(1)
self.runall(checks)
self.assertEqual(len(checks), self.runner.stats.num_cases())
self.assertEqual(0, len(self.runner.stats.failures()))
self.assertEqual(1, max(self.monitor.num_tasks))
self.read_timestamps(self.monitor.tasks)
begin_after_end = (b > e for b, e in zip(self.begin_stamps[1:], self.
    end_stamps[:-1]))
self.assertTrue(all(begin_after_end))
