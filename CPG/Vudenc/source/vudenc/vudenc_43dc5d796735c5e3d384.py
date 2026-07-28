def _create_command(self, **kwargs):...
command = self.executable + ' ' + self.arguments
for key in ('filename', 'config_file'):
kwargs[key] = escape_path_argument(kwargs.get(key, '') or '')
return command.format(**kwargs)
