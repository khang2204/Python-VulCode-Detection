def get_root_path(self):...
"""docstring"""
path = None
if self.main and self.main.projects:
path = self.main.projects.get_active_project_path()
if not path:
path = getcwd_or_home()
return path
