@rt.switch_runtime(fixtures.TEST_SITE_CONFIG, 'sys0')...
find_case = TestDependencies.find_case
cases = executors.generate_testcases(self.loader.load_all())
case0 = find_case('Test0', 'e0', cases)
case1 = find_case('Test0', 'e1', cases)
case0_copy = case0.clone()
assert case0 == case0_copy
assert hash(case0) == hash(case0_copy)
assert case1 != case0
assert hash(case1) != hash(case0)
