def kill_redis(self, check_alive=True):...
"""docstring"""
self._kill_process_type(ray_constants.PROCESS_TYPE_REDIS_SERVER,
    check_alive=check_alive)
