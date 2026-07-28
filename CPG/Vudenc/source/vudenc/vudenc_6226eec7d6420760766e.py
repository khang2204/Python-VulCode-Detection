def start_log_monitor(self):...
"""docstring"""
stdout_file, stderr_file = new_log_monitor_log_file()
process_info = ray.services.start_log_monitor(self.redis_address, self.
    _node_ip_address, stdout_file=stdout_file, stderr_file=stderr_file,
    redis_password=self._ray_params.redis_password)
assert ray_constants.PROCESS_TYPE_LOG_MONITOR not in self.all_processes
self.all_processes[ray_constants.PROCESS_TYPE_LOG_MONITOR] = [process_info]
