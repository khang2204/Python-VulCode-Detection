@rt.switch_runtime(fixtures.TEST_SITE_CONFIG, 'sys0')...
t0 = self.create_test('t0')
t1 = self.create_test('t1')
t2 = self.create_test('t2')
t3 = self.create_test('t3')
t4 = self.create_test('t4')
t1.depends_on('t0')
t2.depends_on('t1')
t3.depends_on('t1')
t3.depends_on('t2')
t4.depends_on('t2')
t4.depends_on('t3')
dependency.validate_deps(dependency.build_deps(executors.generate_testcases
    ([t0, t1, t2, t3, t4])))
