from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import threading
import traceback
import redis
import ray
from ray import ray_constants
from ray import cloudpickle as pickle
from ray import profiling
from ray import utils
"""A thread used to import exports from the driver or other workers.

    Note:
    The driver also has an import thread, which is used only to
    import custom class definitions from calls to register_custom_serializer
    that happen under the hood on workers.

    Attributes:
        worker: the worker object in this process.
        mode: worker mode
        redis_client: the redis client used to query exports.
    """
def __init__(self, worker, mode):...
self.worker = worker
self.mode = mode
self.redis_client = worker.redis_client
def start(self):...
"""docstring"""
t = threading.Thread(target=self._run, name='ray_import_thread')
t.daemon = True
t.start()
def _run(self):...
import_pubsub_client = self.redis_client.pubsub()
import_pubsub_client.subscribe('__keyspace@0__:Exports')
num_imported = 0
export_keys = self.redis_client.lrange('Exports', 0, -1)
for key in export_keys:
num_imported += 1
for msg in import_pubsub_client.listen():
def _process_key(self, key):...
self._process_key(key)
if msg['type'] == 'subscribe':
"""docstring"""
assert msg['data'] == b'rpush'
if self.mode != ray.WORKER_MODE:
num_imports = self.redis_client.llen('Exports')
if key.startswith(b'FunctionsToRun'):
if key.startswith(b'RemoteFunction'):
assert num_imports >= num_imported
self.fetch_and_execute_function_to_run(key)
return
self.worker.function_actor_manager.fetch_and_register_remote_function(key)
if key.startswith(b'FunctionsToRun'):
for i in range(num_imported, num_imports):
def fetch_and_execute_function_to_run(self, key):...
self.fetch_and_execute_function_to_run(key)
if key.startswith(b'ActorClass'):
num_imported += 1
"""docstring"""
self.worker.function_actor_manager.imported_actor_classes.add(key)
key = self.redis_client.lindex('Exports', i)
driver_id, serialized_function, run_on_other_drivers = self.redis_client.hmget(
    key, ['driver_id', 'function', 'run_on_other_drivers'])
self._process_key(key)
if utils.decode(run_on_other_drivers
return
function = pickle.loads(serialized_function)
traceback_str = traceback.format_exc()
function({'worker': self.worker})
utils.push_error_to_driver(self.worker, ray_constants.
    FUNCTION_TO_RUN_PUSH_ERROR, traceback_str, driver_id=ray.DriverID(
    driver_id))
