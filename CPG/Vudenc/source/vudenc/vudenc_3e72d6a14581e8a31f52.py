def start_raylet_monitor(self):...
"""docstring"""
stdout_file, stderr_file = new_raylet_monitor_log_file(self._ray_params.
    redirect_output)
process_info = ray.services.start_raylet_monitor(self._redis_address,
    stdout_file=stdout_file, stderr_file=stderr_file, redis_password=self.
    _ray_params.redis_password, config=self._config)
assert ray_constants.PROCESS_TYPE_RAYLET_MONITOR not in self.all_processes
self.all_processes[ray_constants.PROCESS_TYPE_RAYLET_MONITOR] = [process_info]
