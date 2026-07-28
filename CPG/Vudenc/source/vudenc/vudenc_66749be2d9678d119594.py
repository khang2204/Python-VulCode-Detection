def test_sql_statements(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 12}, 'CONFIDENCE': {'LOW': 7, 'MEDIUM': 5}}
self.check_example('sql_statements.py', expect)
