def test_verbosity_settings_1_process(self):...
"""docstring"""
expected_verbosity_string = (
    '--with-xunit --xunit-file={repo_dir}/reports/bok_choy{shard_str}/xunit.xml --verbosity=2'
    .format(repo_dir=REPO_DIR, shard_str='/shard_' + self.shard if self.
    shard else ''))
suite = BokChoyTestSuite('', num_processes=1)
self.assertEqual(BokChoyTestSuite.verbosity_processes_string(suite),
    expected_verbosity_string)
