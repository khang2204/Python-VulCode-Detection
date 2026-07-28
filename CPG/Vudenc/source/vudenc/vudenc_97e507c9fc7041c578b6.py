@property...
"""docstring"""
stdout = self.stdout_interceptor
stderr = self.stderr_interceptor
return max([self._last_update_time, stdout.last_write_time if stdout else 0,
    stderr.last_write_time if stderr else 0])
