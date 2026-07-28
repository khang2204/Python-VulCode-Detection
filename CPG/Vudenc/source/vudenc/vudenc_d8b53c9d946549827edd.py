from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import argparse
import logging
import os
import time
import traceback
import redis
import ray
from ray.autoscaler.autoscaler import LoadMetrics, StandardAutoscaler
import ray.cloudpickle as pickle
import ray.gcs_utils
import ray.utils
import ray.ray_constants as ray_constants
from ray.services import get_ip_address, get_port
from ray.utils import binary_to_hex, binary_to_object_id, hex_to_binary, setup_logger
logger = logging.getLogger(__name__)
"""A monitor for Ray processes.

    The monitor is in charge of cleaning up the tables in the global state
    after processes have died. The monitor is currently not responsible for
    detecting component failures.

    Attributes:
        redis: A connection to the Redis server.
        subscribe_client: A pubsub client for the Redis server. This is used to
            receive notifications about failed components.
    """
def __init__(self, redis_address, redis_port, autoscaling_config,...
self.state = ray.experimental.state.GlobalState()
self.state._initialize_global_state(redis_address, redis_port,
    redis_password=redis_password)
self.redis = redis.StrictRedis(host=redis_address, port=redis_port, db=0,
    password=redis_password)
self.primary_subscribe_client = self.redis.pubsub(ignore_subscribe_messages
    =True)
self.local_scheduler_id_to_ip_map = {}
self.load_metrics = LoadMetrics()
if autoscaling_config:
self.autoscaler = StandardAutoscaler(autoscaling_config, self.load_metrics)
self.autoscaler = None
self.issue_gcs_flushes = 'RAY_USE_NEW_GCS' in os.environ
self.gcs_flush_policy = None
if self.issue_gcs_flushes:
addr_port = self.redis.lrange('RedisShards', 0, -1)
def subscribe(self, channel):...
if len(addr_port) > 1:
"""docstring"""
logger.warning(
    'Monitor: TODO: if launching > 1 redis shard, flushing needs to touch shards in parallel.'
    )
addr_port = addr_port[0].split(b':')
self.primary_subscribe_client.subscribe(channel)
self.issue_gcs_flushes = False
self.redis_shard = redis.StrictRedis(host=addr_port[0], port=addr_port[1],
    password=redis_password)
def xray_heartbeat_batch_handler(self, unused_channel, data):...
self.redis_shard.execute_command('HEAD.FLUSH 0')
logger.info('Monitor: Turning off flushing due to exception: {}'.format(str(e))
    )
"""docstring"""
self.issue_gcs_flushes = False
gcs_entries = ray.gcs_utils.GcsTableEntry.GetRootAsGcsTableEntry(data, 0)
heartbeat_data = gcs_entries.Entries(0)
message = (ray.gcs_utils.HeartbeatBatchTableData.
    GetRootAsHeartbeatBatchTableData(heartbeat_data, 0))
for j in range(message.BatchLength()):
heartbeat_message = message.Batch(j)
def _xray_clean_up_entries_for_driver(self, driver_id):...
num_resources = heartbeat_message.ResourcesAvailableLabelLength()
"""docstring"""
static_resources = {}
xray_task_table_prefix = ray.gcs_utils.TablePrefix_RAYLET_TASK_string.encode(
    'ascii')
dynamic_resources = {}
xray_object_table_prefix = ray.gcs_utils.TablePrefix_OBJECT_string.encode(
    'ascii')
for i in range(num_resources):
task_table_objects = self.state.task_table()
dyn = heartbeat_message.ResourcesAvailableLabel(i)
client_id = ray.utils.binary_to_hex(heartbeat_message.ClientId())
driver_id_hex = binary_to_hex(driver_id)
static = heartbeat_message.ResourcesTotalLabel(i)
ip = self.local_scheduler_id_to_ip_map.get(client_id)
driver_task_id_bins = set()
dynamic_resources[dyn] = heartbeat_message.ResourcesAvailableCapacity(i)
if ip:
for task_id_hex, task_info in task_table_objects.items():
static_resources[static] = heartbeat_message.ResourcesTotalCapacity(i)
self.load_metrics.update(ip, static_resources, dynamic_resources)
logger.warning('Monitor: could not find ip for client {}'.format(client_id))
task_table_object = task_info['TaskSpec']
object_table_objects = self.state.object_table()
task_driver_id_hex = task_table_object['DriverID']
driver_object_id_bins = set()
if driver_id_hex != task_driver_id_hex:
for object_id, _ in object_table_objects.items():
driver_task_id_bins.add(hex_to_binary(task_id_hex))
task_id_bin = ray._raylet.compute_task_id(object_id).binary()
def to_shard_index(id_bin):...
if task_id_bin in driver_task_id_bins:
return binary_to_object_id(id_bin).redis_shard_hash() % len(self.state.
    redis_clients)
driver_object_id_bins.add(object_id.binary())
