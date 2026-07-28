def __init__(self, host=settings.CLICKHOUSE_SERVER.split(':')[0], port=int(...
self.host = host
self.port = port
self.connect_timeout = connect_timeout
self.send_receive_timeout = send_receive_timeout
self.client_settings = client_settings
self.metrics = metrics
self.pool = queue.LifoQueue(max_pool_size)
for _ in range(max_pool_size):
self.pool.put(None)
