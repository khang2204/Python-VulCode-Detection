def remove_sos_archive(self):...
"""docstring"""
if self.sos_path is None:
return
if 'sosreport' not in self.sos_path:
self.log_debug(
    'Node sosreport path %s looks incorrect. Not attempting to remove path' %
    self.sos_path)
removed = self.remove_file(self.sos_path)
return
if not removed:
self.log_error('Failed to remove sosreport')
