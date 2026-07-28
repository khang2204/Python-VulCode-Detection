def start_ray_processes(self):...
"""docstring"""
set_temp_root(self._ray_params.temp_dir)
logger.info('Process STDOUT and STDERR is being redirected to {}.'.format(
    get_logs_dir_path()))
if self._redis_address is None:
self.start_redis()
self.start_plasma_store()
self.start_monitor()
self.start_raylet()
self.start_raylet_monitor()
if self._ray_params.include_log_monitor:
self.start_log_monitor()
if self._ray_params.include_webui:
self.start_ui()
