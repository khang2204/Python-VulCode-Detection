def test_pass_in_retries(self):...
max_retries = 3
run_to_pass = 2
fp.write('0\n')
checks = [RetriesCheck(run_to_pass, fp.name)]
self.runner._max_retries = max_retries
self.runall(checks)
self.assertEqual(1, self.runner.stats.num_cases())
self.assertEqual(1, len(self.runner.stats.failures(run=0)))
self.assertEqual(run_to_pass, rt.runtime().current_run)
self.assertEqual(0, len(self.runner.stats.failures()))
os.remove(fp.name)
