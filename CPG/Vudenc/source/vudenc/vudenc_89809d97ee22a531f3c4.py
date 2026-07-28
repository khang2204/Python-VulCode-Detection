def test_runall_skip_system_check(self):...
self.runall(self.checks, skip_system_check=True)
stats = self.runner.stats
self.assertEqual(8, stats.num_cases())
self.assertEqual(4, len(stats.failures()))
self.assertEqual(2, self._num_failures_stage('setup'))
self.assertEqual(1, self._num_failures_stage('sanity'))
self.assertEqual(1, self._num_failures_stage('performance'))
