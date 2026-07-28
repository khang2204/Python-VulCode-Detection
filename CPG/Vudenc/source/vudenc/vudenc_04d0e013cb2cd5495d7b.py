def kill_raylet(self, check_alive=True):...
"""docstring"""
self._kill_process_type(ray_constants.PROCESS_TYPE_RAYLET, check_alive=
    check_alive)
