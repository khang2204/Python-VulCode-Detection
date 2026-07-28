def _maybe_flush_gcs(self):...
"""docstring"""
if not self.issue_gcs_flushes:
return
if self.gcs_flush_policy is None:
serialized = self.redis.get('gcs_flushing_policy')
if not self.gcs_flush_policy.should_flush(self.redis_shard):
if serialized is None:
return
max_entries_to_flush = self.gcs_flush_policy.num_entries_to_flush()
return
self.gcs_flush_policy = pickle.loads(serialized)
num_flushed = self.redis_shard.execute_command('HEAD.FLUSH {}'.format(
    max_entries_to_flush))
logger.info('Monitor: num_flushed {}'.format(num_flushed))
ray.experimental.flush_redis_unsafe(self.redis)
self.gcs_flush_policy.record_flush()
