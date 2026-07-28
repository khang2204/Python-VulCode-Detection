@rt.switch_runtime(fixtures.TEST_SITE_CONFIG, 'sys0')...
find_check = TestDependencies.find_check
num_deps = TestDependencies.num_deps
checks = self.loader.load_all()
test0 = find_check('Test0', checks)
test1 = find_check('Test1_default', checks)
test1.depends_on('Test0', rfm.DEPEND_EXACT, {'eX': ['e0']})
deps = dependency.build_deps(executors.generate_testcases(checks))
assert num_deps(deps, 'Test1_default') == 4
