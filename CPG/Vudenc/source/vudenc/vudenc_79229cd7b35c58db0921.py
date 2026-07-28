def kill_raylet_monitor(self, check_alive=True):...
"""docstring"""
self._kill_process_type(ray_constants.PROCESS_TYPE_RAYLET_MONITOR,
    check_alive=check_alive)
