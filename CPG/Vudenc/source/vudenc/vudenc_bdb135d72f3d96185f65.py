def get_full_path(self, filename, language=None, version_slug=None):...
"""docstring"""
if re.match('^https?://', filename):
return filename
return resolve_path(project=self.project, language=language, version_slug=
    version_slug, filename=filename)
