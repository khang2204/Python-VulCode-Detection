def test_code_line_numbers(self):...
self.run_example('binding.py')
issues = self.b_mgr.get_issue_list()
code_lines = issues[0].get_code().splitlines()
lineno = issues[0].lineno
self.assertEqual('%i ' % (lineno - 1), code_lines[0][:2])
self.assertEqual('%i ' % lineno, code_lines[1][:2])
self.assertEqual('%i ' % (lineno + 1), code_lines[2][:2])
