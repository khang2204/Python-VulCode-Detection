def test_verbosity_settings_2_processes(self):...
"""docstring"""
process_count = 2
expected_verbosity_string = (
    '--with-xunitmp --xunitmp-file={repo_dir}/reports/bok_choy{shard_str}/xunit.xml --processes={procs} --no-color --process-timeout=1200'
    .format(repo_dir=REPO_DIR, shard_str='/shard_' + self.shard if self.
    shard else '', procs=process_count))
suite = BokChoyTestSuite('', num_processes=process_count)
self.assertEqual(BokChoyTestSuite.verbosity_processes_string(suite),
    expected_verbosity_string)
