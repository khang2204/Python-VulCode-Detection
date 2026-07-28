def _get_archive_path(self):...
"""docstring"""
self.arc_name = self._get_archive_name()
compr = 'gz'
return self.config['out_dir'] + self.arc_name + '.tar.' + compr
