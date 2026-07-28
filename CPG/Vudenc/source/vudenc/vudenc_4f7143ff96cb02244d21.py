def test_try_except_pass(self):...
"""docstring"""
test = next(x for x in self.b_mgr.b_ts.tests['ExceptHandler'] if x.__name__ ==
    'try_except_pass')
test._config = {'check_typed_exception': True}
expect = {'SEVERITY': {'LOW': 3}, 'CONFIDENCE': {'HIGH': 3}}
self.check_example('try_except_pass.py', expect)
test._config = {'check_typed_exception': False}
expect = {'SEVERITY': {'LOW': 2}, 'CONFIDENCE': {'HIGH': 2}}
self.check_example('try_except_pass.py', expect)
