def clean(self):...
cleaned_data = super().clean()
if 'path' in cleaned_data:
validate_unique_project_path(self.instance.project, cleaned_data['path'],
    self.instance.pk)
return cleaned_data
