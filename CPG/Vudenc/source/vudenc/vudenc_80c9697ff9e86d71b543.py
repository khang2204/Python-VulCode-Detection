def _update_priority(self):...
exists = Priority.objects.filter(pk=self.new_value).exists()
if not exists:
self.get_update_targets().update(**{str(self.target_field): self.new_value})
