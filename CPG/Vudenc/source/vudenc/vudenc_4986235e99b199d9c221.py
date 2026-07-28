def suffix_version(self, name):...
"""docstring"""
if self.version == 'custom':
suffix = self.get_options().suffix_version
if name.endswith(self.version):
if suffix:
return '{0}_{1}'.format(name, self.version)
return '{0}_{1}'.format(name, suffix)
