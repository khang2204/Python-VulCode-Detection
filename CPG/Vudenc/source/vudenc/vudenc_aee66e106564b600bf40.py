def _run_checks(self, checks, max_jobs):...
self.set_max_jobs(max_jobs)
self.assertRaises(KeyboardInterrupt, self.runall, checks)
self.assertEqual(4, self.runner.stats.num_cases())
self.assertEqual(4, len(self.runner.stats.failures()))
self.assert_all_dead()
