def start_raylet(self, use_valgrind=False, use_profiler=False):...
"""docstring"""
assert self._raylet_socket_name is None
self._raylet_socket_name = (self._ray_params.raylet_socket_name or
    get_raylet_socket_name())
self.prepare_socket_file(self._raylet_socket_name)
stdout_file, stderr_file = new_raylet_log_file(redirect_output=self.
    _ray_params.redirect_worker_output)
process_info = ray.services.start_raylet(self._redis_address, self.
    _node_ip_address, self._raylet_socket_name, self.
    _plasma_store_socket_name, self._ray_params.worker_path, self.
    _ray_params.num_cpus, self._ray_params.num_gpus, self._ray_params.
    resources, self._ray_params.object_manager_port, self._ray_params.
    node_manager_port, self._ray_params.redis_password, use_valgrind=
    use_valgrind, use_profiler=use_profiler, stdout_file=stdout_file,
    stderr_file=stderr_file, config=self._config, include_java=self.
    _ray_params.include_java, java_worker_options=self._ray_params.
    java_worker_options)
assert ray_constants.PROCESS_TYPE_RAYLET not in self.all_processes
self.all_processes[ray_constants.PROCESS_TYPE_RAYLET] = [process_info]
