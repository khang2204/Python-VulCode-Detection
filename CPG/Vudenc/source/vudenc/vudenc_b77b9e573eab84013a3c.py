def _xray_clean_up_entries_for_driver(self, driver_id):...
"""docstring"""
xray_task_table_prefix = ray.gcs_utils.TablePrefix_RAYLET_TASK_string.encode(
    'ascii')
xray_object_table_prefix = ray.gcs_utils.TablePrefix_OBJECT_string.encode(
    'ascii')
task_table_objects = self.state.task_table()
driver_id_hex = binary_to_hex(driver_id)
driver_task_id_bins = set()
for task_id_hex, task_info in task_table_objects.items():
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
