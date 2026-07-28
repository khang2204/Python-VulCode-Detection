def test_retries_good_check(self):...
max_retries = 2
checks = [HelloTest()]
self.runner._max_retries = max_retries
self.runall(checks)
self.assertEqual(1, self.runner.stats.num_cases())
self.assertEqual(0, rt.runtime().current_run)
self.assertEqual(0, len(self.runner.stats.failures()))
