def kill_plasma_store(self, check_alive=True):...
"""docstring"""
self._kill_process_type(ray_constants.PROCESS_TYPE_PLASMA_STORE,
    check_alive=check_alive)
