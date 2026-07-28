@rt.switch_runtime(fixtures.TEST_SITE_CONFIG, 'sys0')...
Node = TestDependencies.Node
has_edge = TestDependencies.has_edge
num_deps = TestDependencies.num_deps
find_check = TestDependencies.find_check
find_case = TestDependencies.find_case
checks = self.loader.load_all()
cases = executors.generate_testcases(checks)
t = find_check('Test1_exact', checks)
t.getdep('Test0', 'e0')
deps = dependency.build_deps(cases)
dependency.validate_deps(deps)
assert num_deps(deps, 'Test1_fully') == 8
for p in ['sys0:p0', 'sys0:p1']:
for e0 in ['e0', 'e1']:
assert num_deps(deps, 'Test1_by_env') == 4
for e1 in ['e0', 'e1']:
assert num_deps(deps, 'Test1_default') == 4
assert has_edge(deps, Node('Test1_fully', p, e0), Node('Test0', p, e1))
for p in ['sys0:p0', 'sys0:p1']:
for e in ['e0', 'e1']:
assert num_deps(deps, 'Test1_exact') == 6
assert has_edge(deps, Node('Test1_by_env', p, e), Node('Test0', p, e))
for p in ['sys0:p0', 'sys0:p1']:
assert has_edge(deps, Node('Test1_default', p, e), Node('Test0', p, e))
assert has_edge(deps, Node('Test1_exact', p, 'e0'), Node('Test0', p, 'e0'))
check_e0 = find_case('Test1_exact', 'e0', cases).check
assert has_edge(deps, Node('Test1_exact', p, 'e0'), Node('Test0', p, 'e1'))
check_e1 = find_case('Test1_exact', 'e1', cases).check
assert has_edge(deps, Node('Test1_exact', p, 'e1'), Node('Test0', p, 'e1'))
assert check_e0.getdep('Test0', 'e0').name == 'Test0'
assert check_e0.getdep('Test0', 'e1').name == 'Test0'
assert check_e1.getdep('Test0', 'e1').name == 'Test0'
check_e0.getdep('TestX', 'e0')
check_e0.getdep('Test0', 'eX')
check_e1.getdep('Test0', 'e0')
