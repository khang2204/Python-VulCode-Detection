def run(self, **kwargs):...
"""docstring"""
env, kwargs = self._prepare_env(kwargs)
return subprocess.Popen(self.cmd, env=env, **kwargs)
