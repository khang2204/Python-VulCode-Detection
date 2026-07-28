def check(self, **kwargs):...
errors = super().check(**kwargs)
if self.base_field.remote_field:
errors.append(checks.Error(
    'Base field for array cannot be a related field.', obj=self, id=
    'postgres.E002'))
base_errors = self.base_field.check()
return errors
if base_errors:
messages = '\n    '.join('%s (%s)' % (error.msg, error.id) for error in
    base_errors)
errors.append(checks.Error("""Base field for array has errors:
    %s""" %
    messages, obj=self, id='postgres.E001'))
