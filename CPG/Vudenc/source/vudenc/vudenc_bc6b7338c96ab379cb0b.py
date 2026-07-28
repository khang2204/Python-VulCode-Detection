def test_system_exit_within_test(self):...
check = SystemExitCheck()
self.runall([check])
stats = self.runner.stats
self.assertEqual(1, len(stats.failures()))
