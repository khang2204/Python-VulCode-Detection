def _ValidateInput(self, step_name, test_name, bug_id):...
"""docstring"""
if not step_name:
return self.CreateError('Step name must be specified', 400)
if not test_name:
return self.CreateError('Test name must be specified', 400)
if bug_id and not bug_id.isdigit():
return self.CreateError('Bug id must be an int', 400)
return None
