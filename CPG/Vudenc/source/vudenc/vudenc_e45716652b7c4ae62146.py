def xray_heartbeat_batch_handler(self, unused_channel, data):...
"""docstring"""
gcs_entries = ray.gcs_utils.GcsTableEntry.GetRootAsGcsTableEntry(data, 0)
heartbeat_data = gcs_entries.Entries(0)
message = (ray.gcs_utils.HeartbeatBatchTableData.
    GetRootAsHeartbeatBatchTableData(heartbeat_data, 0))
for j in range(message.BatchLength()):
heartbeat_message = message.Batch(j)
num_resources = heartbeat_message.ResourcesAvailableLabelLength()
static_resources = {}
dynamic_resources = {}
for i in range(num_resources):
dyn = heartbeat_message.ResourcesAvailableLabel(i)
client_id = ray.utils.binary_to_hex(heartbeat_message.ClientId())
static = heartbeat_message.ResourcesTotalLabel(i)
ip = self.local_scheduler_id_to_ip_map.get(client_id)
dynamic_resources[dyn] = heartbeat_message.ResourcesAvailableCapacity(i)
if ip:
static_resources[static] = heartbeat_message.ResourcesTotalCapacity(i)
self.load_metrics.update(ip, static_resources, dynamic_resources)
logger.warning('Monitor: could not find ip for client {}'.format(client_id))
