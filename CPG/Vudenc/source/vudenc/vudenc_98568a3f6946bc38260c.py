def start_ui(self):...
"""docstring"""
stdout_file, stderr_file = new_webui_log_file()
self._webui_url, process_info = ray.services.start_ui(self._redis_address,
    stdout_file=stdout_file, stderr_file=stderr_file)
assert ray_constants.PROCESS_TYPE_WEB_UI not in self.all_processes
if process_info is not None:
self.all_processes[ray_constants.PROCESS_TYPE_WEB_UI] = [process_info]
