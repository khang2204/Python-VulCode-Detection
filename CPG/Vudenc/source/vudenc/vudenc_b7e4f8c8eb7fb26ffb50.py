@rt.switch_runtime(fixtures.TEST_SITE_CONFIG, 'sys0')...
find_check = TestDependencies.find_check
checks = self.loader.load_all()
test0 = find_check('Test0', checks)
test1 = find_check('Test1_default', checks)
test1.depends_on('Test0', rfm.DEPEND_EXACT, {'e0': ['eX']})
dependency.build_deps(executors.generate_testcases(checks))
