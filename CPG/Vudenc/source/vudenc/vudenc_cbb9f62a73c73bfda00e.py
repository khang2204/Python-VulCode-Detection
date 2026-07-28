def test_strict_performance_check(self):...
self.runner.policy.strict_check = True
self.runall(self.checks)
stats = self.runner.stats
self.assertEqual(7, stats.num_cases())
self.assertEqual(5, len(stats.failures()))
self.assertEqual(2, self._num_failures_stage('setup'))
self.assertEqual(1, self._num_failures_stage('sanity'))
self.assertEqual(2, self._num_failures_stage('performance'))
