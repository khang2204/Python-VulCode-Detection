def execute_robust(self, *args, **kwargs):...
retries = 3
while True:
return self.execute(*args, **kwargs)
logger.warning('Write to ClickHouse failed: %s (%d retries)', str(e), retries)
if retries <= 0:
retries -= 1
if self.metrics:
self.metrics.increment('clickhouse.network-error')
time.sleep(1)
logger.warning('Write to ClickHouse failed: %s (retrying)', str(e))
if e.code == errors.ErrorCodes.TOO_MANY_SIMULTANEOUS_QUERIES:
if self.metrics:
self.metrics.increment('clickhouse.too-many-queries')
time.sleep(1)
