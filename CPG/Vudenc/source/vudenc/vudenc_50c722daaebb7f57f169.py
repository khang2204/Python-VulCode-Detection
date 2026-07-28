@rt.switch_runtime(fixtures.TEST_SITE_CONFIG, 'sys0')...
find_check = TestDependencies.find_check
checks = self.loader.load_all()
test0 = find_check('Test0', checks)
for depkind in ('default', 'fully', 'by_env', 'exact'):
test1 = find_check('Test1_' + depkind, checks)
if depkind == 'default':
test1.depends_on('TestX')
if depkind == 'exact':
dependency.build_deps(executors.generate_testcases(checks))
test1.depends_on('TestX', rfm.DEPEND_EXACT, {'e0': ['e0']})
if depkind == 'fully':
test1.depends_on('TestX', rfm.DEPEND_FULLY)
if depkind == 'by_env':
test1.depends_on('TestX', rfm.DEPEND_BY_ENV)
