def start_plasma_store(self):...
"""docstring"""
assert self._plasma_store_socket_name is None
self._plasma_store_socket_name = (self._ray_params.plasma_store_socket_name or
    get_object_store_socket_name())
self.prepare_socket_file(self._plasma_store_socket_name)
stdout_file, stderr_file = new_plasma_store_log_file(self._ray_params.
    redirect_output)
process_info = ray.services.start_plasma_store(self._node_ip_address, self.
    _redis_address, stdout_file=stdout_file, stderr_file=stderr_file,
    object_store_memory=self._ray_params.object_store_memory,
    plasma_directory=self._ray_params.plasma_directory, huge_pages=self.
    _ray_params.huge_pages, plasma_store_socket_name=self.
    _plasma_store_socket_name, redis_password=self._ray_params.redis_password)
assert ray_constants.PROCESS_TYPE_PLASMA_STORE not in self.all_processes
self.all_processes[ray_constants.PROCESS_TYPE_PLASMA_STORE] = [process_info]
