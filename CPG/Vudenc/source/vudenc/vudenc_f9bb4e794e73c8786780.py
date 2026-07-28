@rt.switch_runtime(fixtures.TEST_SITE_CONFIG, 'sys0')...
t0 = self.create_test('t0')
t1 = self.create_test('t1')
t1.depends_on('t0', rfm.DEPEND_EXACT, {'e0': ['e0']})
t0.depends_on('t1', rfm.DEPEND_EXACT, {'e1': ['e1']})
deps = dependency.build_deps(executors.generate_testcases([t0, t1]))
dependency.validate_deps(deps)
assert 't1->t0->t1' in str(exc_info.value) or 't0->t1->t0' in str(exc_info.
    value)
