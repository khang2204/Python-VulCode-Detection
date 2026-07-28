@rt.switch_runtime(fixtures.TEST_SITE_CONFIG, 'sys0')...
t0 = self.create_test('t0')
t1 = self.create_test('t1')
t2 = self.create_test('t2')
t3 = self.create_test('t3')
t4 = self.create_test('t4')
t1.depends_on('t0')
t1.depends_on('t4')
t2.depends_on('t1')
t3.depends_on('t1')
t3.depends_on('t2')
t4.depends_on('t2')
t4.depends_on('t3')
deps = dependency.build_deps(executors.generate_testcases([t0, t1, t2, t3, t4])
    )
dependency.validate_deps(deps)
assert 't4->t2->t1->t4' in str(exc_info.value) or 't2->t1->t4->t2' in str(
    exc_info.value) or 't1->t4->t2->t1' in str(exc_info.value
    ) or 't1->t4->t3->t1' in str(exc_info.value) or 't4->t3->t1->t4' in str(
    exc_info.value) or 't3->t1->t4->t3' in str(exc_info.value)
