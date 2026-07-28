def kill_all_processes(self, check_alive=True, allow_graceful=False):...
"""docstring"""
if ray_constants.PROCESS_TYPE_RAYLET in self.all_processes:
self._kill_process_type(ray_constants.PROCESS_TYPE_RAYLET, check_alive=
    check_alive, allow_graceful=allow_graceful)
for process_type in list(self.all_processes.keys()):
self._kill_process_type(process_type, check_alive=check_alive,
    allow_graceful=allow_graceful)
