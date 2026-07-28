def check_output(self, **kwargs):...
"""docstring"""
env, kwargs = self._prepare_env(kwargs)
return subprocess.check_output(self.cmd, env=env, **kwargs)
