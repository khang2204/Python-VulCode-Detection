def test_runall_skip_performance_check(self):...
self.runner.policy.skip_performance_check = True
self.runall(self.checks)
stats = self.runner.stats
self.assertEqual(7, stats.num_cases())
self.assertEqual(3, len(stats.failures()))
self.assertEqual(2, self._num_failures_stage('setup'))
self.assertEqual(1, self._num_failures_stage('sanity'))
self.assertEqual(0, self._num_failures_stage('performance'))
