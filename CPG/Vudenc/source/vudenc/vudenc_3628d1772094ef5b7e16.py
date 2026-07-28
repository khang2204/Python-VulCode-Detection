def test_retries_bad_check(self):...
max_retries = 2
checks = [BadSetupCheck(), BadSetupCheckEarly()]
self.runner._max_retries = max_retries
self.runall(checks)
self.assertEqual(2, self.runner.stats.num_cases())
self.assertEqual(max_retries, rt.runtime().current_run)
self.assertEqual(2, len(self.runner.stats.failures()))
self.runner.stats.retry_report()
