def exec_conditions(self, conditions, prefix):...
"""docstring"""
if conditions:
for rec in self:
is_valid = safe_eval(conditions, {'object': rec, 'env': self.env})
logging.error('CRAPO: Failed to validate transition %sconditions: %s',
    prefix, str(err))
if not is_valid:
is_valid = False
