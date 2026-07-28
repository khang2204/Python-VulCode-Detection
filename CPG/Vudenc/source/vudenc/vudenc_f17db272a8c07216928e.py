def test_invalid_verbosity_and_processes(self):...
"""docstring"""
suite = BokChoyTestSuite('', num_processes=2, verbosity=3)
BokChoyTestSuite.verbosity_processes_string(suite)
