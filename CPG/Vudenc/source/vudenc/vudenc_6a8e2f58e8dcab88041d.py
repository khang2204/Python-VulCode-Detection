def start_redis(self):...
"""docstring"""
assert self._redis_address is None
self._redis_address, redis_shards, process_infos = ray.services.start_redis(
    self._node_ip_address, port=self._ray_params.redis_port,
    redis_shard_ports=self._ray_params.redis_shard_ports, num_redis_shards=
    self._ray_params.num_redis_shards, redis_max_clients=self._ray_params.
    redis_max_clients, redirect_output=self._ray_params.redirect_output,
    redirect_worker_output=self._ray_params.redirect_worker_output,
    password=self._ray_params.redis_password, redis_max_memory=self.
    _ray_params.redis_max_memory)
assert ray_constants.PROCESS_TYPE_REDIS_SERVER not in self.all_processes
self.all_processes[ray_constants.PROCESS_TYPE_REDIS_SERVER] = process_infos
