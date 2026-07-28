def _run(self):...
import_pubsub_client = self.redis_client.pubsub()
import_pubsub_client.subscribe('__keyspace@0__:Exports')
num_imported = 0
export_keys = self.redis_client.lrange('Exports', 0, -1)
for key in export_keys:
num_imported += 1
for msg in import_pubsub_client.listen():
self._process_key(key)
if msg['type'] == 'subscribe':
assert msg['data'] == b'rpush'
num_imports = self.redis_client.llen('Exports')
assert num_imports >= num_imported
for i in range(num_imported, num_imports):
num_imported += 1
key = self.redis_client.lindex('Exports', i)
self._process_key(key)
