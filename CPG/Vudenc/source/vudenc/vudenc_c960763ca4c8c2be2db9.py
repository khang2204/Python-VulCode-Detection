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
if len(addr_port) > 1:
logger.warning(
    'Monitor: TODO: if launching > 1 redis shard, flushing needs to touch shards in parallel.'
    )
addr_port = addr_port[0].split(b':')
self.issue_gcs_flushes = False
self.redis_shard = redis.StrictRedis(host=addr_port[0], port=addr_port[1],
    password=redis_password)
self.redis_shard.execute_command('HEAD.FLUSH 0')
logger.info('Monitor: Turning off flushing due to exception: {}'.format(str(e))
    )
self.issue_gcs_flushes = False
