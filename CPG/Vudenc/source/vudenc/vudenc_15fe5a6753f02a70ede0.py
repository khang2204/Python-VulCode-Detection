def _prepare_env(self, kwargs):...
"""docstring"""
kwargs = kwargs.copy()
env = kwargs.pop('env', os.environ).copy()
env['PATH'] = self.bin_dir_path + os.path.pathsep + env['PATH'] if env.get(
    'PATH', '') else self.bin_dir_path
return env, kwargs
