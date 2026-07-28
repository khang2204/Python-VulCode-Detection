def process_messages(self, max_messages=10000):...
"""docstring"""
subscribe_clients = [self.primary_subscribe_client]
for subscribe_client in subscribe_clients:
for _ in range(max_messages):
message = subscribe_client.get_message()
if message is None:
channel = message['channel']
data = message['data']
if channel == ray.gcs_utils.XRAY_HEARTBEAT_BATCH_CHANNEL:
message_handler = self.xray_heartbeat_batch_handler
if channel == ray.gcs_utils.XRAY_DRIVER_CHANNEL:
message_handler(channel, data)
message_handler = self.xray_driver_removed_handler
