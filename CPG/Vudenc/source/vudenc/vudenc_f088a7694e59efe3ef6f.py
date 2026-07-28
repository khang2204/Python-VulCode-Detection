def test_concurrency_limited(self):...
checks = [SleepCheck(0.5) for i in range(5)]
max_jobs = len(checks) - 2
self.set_max_jobs(max_jobs)
self.runall(checks)
self.assertEqual(len(checks), self.runner.stats.num_cases())
self.assertEqual(0, len(self.runner.stats.failures()))
self.assertEqual(max_jobs, max(self.monitor.num_tasks))
self.assertEqual(max_jobs, self.monitor.num_tasks[max_jobs])
self.read_timestamps(self.monitor.tasks)
begin_after_end = (b > e for b, e in zip(self.begin_stamps[max_jobs:], self
    .end_stamps[:-max_jobs]))
self.assertTrue(all(begin_after_end))
if self.begin_stamps[max_jobs - 1] > self.end_stamps[0]:
self.skipTest('the system seems too loaded.')
