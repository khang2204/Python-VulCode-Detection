@property...
"""docstring"""
if not self.project:
return ''
return os.path.join(self.project.results_path, '.cache', 'steps', '{}.json'
    .format(self.id))
