def _update_reviewer(self):...
reviewers = User.objects.filter(username=self.new_value).values_list('pk',
    flat=True)
if not reviewers:
err_msg = 'Reviewer %s is not found' % self.new_value
self.get_update_targets().update(**{str(self.target_field): reviewers[0]})
