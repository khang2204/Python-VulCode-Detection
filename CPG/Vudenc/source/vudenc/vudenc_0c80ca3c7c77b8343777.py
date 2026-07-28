def test_runall(self):...
self.runall(self.checks)
stats = self.runner.stats
self.assertEqual(7, stats.num_cases())
self.assertEqual(4, len(stats.failures()))
self.assertEqual(2, self._num_failures_stage('setup'))
self.assertEqual(1, self._num_failures_stage('sanity'))
self.assertEqual(1, self._num_failures_stage('performance'))
