def __init__(self, ray_params, head=False, shutdown_at_exit=True):...
"""docstring"""
self.all_processes = {}
ray_params.update_if_absent(node_ip_address=ray.services.
    get_node_ip_address(), include_log_monitor=True, resources={},
    include_webui=False, worker_path=os.path.join(os.path.dirname(os.path.
    abspath(__file__)), 'workers/default_worker.py'))
if head:
ray_params.update_if_absent(num_redis_shards=1, include_webui=True)
redis_client = ray.services.create_redis_client(ray_params.redis_address,
    ray_params.redis_password)
self._ray_params = ray_params
ray_params.include_java = ray.services.include_java_from_redis(redis_client)
self._config = json.loads(ray_params._internal_config
    ) if ray_params._internal_config else None
self._node_ip_address = ray_params.node_ip_address
self._redis_address = ray_params.redis_address
self._plasma_store_socket_name = None
self._raylet_socket_name = None
self._webui_url = None
self.start_ray_processes()
if shutdown_at_exit:
atexit.register(lambda : self.kill_all_processes(check_alive=False,
    allow_graceful=True))
