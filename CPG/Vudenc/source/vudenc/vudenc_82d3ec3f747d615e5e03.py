from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import atexit
import json
import os
import logging
import signal
import threading
import time
import ray
import ray.ray_constants as ray_constants
from ray.tempfile_services import get_logs_dir_path, get_object_store_socket_name, get_raylet_socket_name, new_log_monitor_log_file, new_monitor_log_file, new_raylet_monitor_log_file, new_plasma_store_log_file, new_raylet_log_file, new_webui_log_file, set_temp_root, try_to_create_directory
logger = logging.getLogger(__name__)
"""An encapsulation of the Ray processes on a single node.

    This class is responsible for starting Ray processes and killing them.

    Attributes:
        all_processes (dict): A mapping from process type (str) to a list of
            ProcessInfo objects. All lists have length one except for the Redis
            server list, which has multiple.
    """
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
@property...
"""docstring"""
return self._node_ip_address
