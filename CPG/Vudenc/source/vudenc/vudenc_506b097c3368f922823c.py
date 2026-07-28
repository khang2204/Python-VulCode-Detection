def start_monitor(self):...
"""docstring"""
stdout_file, stderr_file = new_monitor_log_file(self._ray_params.
    redirect_output)
process_info = ray.services.start_monitor(self._redis_address, self.
    _node_ip_address, stdout_file=stdout_file, stderr_file=stderr_file,
    autoscaling_config=self._ray_params.autoscaling_config, redis_password=
    self._ray_params.redis_password)
assert ray_constants.PROCESS_TYPE_MONITOR not in self.all_processes
self.all_processes[ray_constants.PROCESS_TYPE_MONITOR] = [process_info]
