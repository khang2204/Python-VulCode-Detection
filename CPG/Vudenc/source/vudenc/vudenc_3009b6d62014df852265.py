def __init__(self, yml):...
self.yml = yml
self.aws_access_key_id = self._cfg('aws credentials aws_access_key_id'
    ) or os.environ.get('AWS_ACCESS_KEY_ID')
self.aws_secret_access_key = self._cfg('aws credentials aws_secret_access_key'
    ) or os.environ.get('AWS_SECRET_ACCESS_KEY')
self.queue_cfg = self.yml['queue']
self.store_type = self._cfg('store type')
self.s3_bucket = self._cfg('store name')
self.s3_reduced_redundancy = self._cfg('store reduced-redundancy')
self.s3_path = self._cfg('store path')
self.s3_date_prefix = self._cfg('store date-prefix')
self.s3_delete_retry_interval = self._cfg('store delete-retry-interval')
seed_cfg = self.yml['tiles']['seed']
self.seed_all_zoom_start = seed_cfg['all']['zoom-start']
self.seed_all_zoom_until = seed_cfg['all']['zoom-until']
self.seed_n_threads = seed_cfg['n-threads']
seed_metro_cfg = seed_cfg['metro-extract']
self.seed_metro_extract_url = seed_metro_cfg['url']
self.seed_metro_extract_zoom_start = seed_metro_cfg['zoom-start']
self.seed_metro_extract_zoom_until = seed_metro_cfg['zoom-until']
self.seed_metro_extract_cities = seed_metro_cfg['cities']
seed_top_tiles_cfg = seed_cfg['top-tiles']
self.seed_top_tiles_url = seed_top_tiles_cfg['url']
self.seed_top_tiles_zoom_start = seed_top_tiles_cfg['zoom-start']
self.seed_top_tiles_zoom_until = seed_top_tiles_cfg['zoom-until']
toi_store_cfg = self.yml['toi-store']
self.toi_store_type = toi_store_cfg['type']
if self.toi_store_type == 's3':
self.toi_store_s3_bucket = toi_store_cfg['s3']['bucket']
if self.toi_store_type == 'file':
self.toi_store_s3_key = toi_store_cfg['s3']['key']
self.toi_store_file_name = toi_store_cfg['file']['name']
self.seed_should_add_to_tiles_of_interest = seed_cfg[
    'should-add-to-tiles-of-interest']
seed_custom = seed_cfg['custom']
self.seed_custom_zoom_start = seed_custom['zoom-start']
self.seed_custom_zoom_until = seed_custom['zoom-until']
self.seed_custom_bboxes = seed_custom['bboxes']
if self.seed_custom_bboxes:
for bbox in self.seed_custom_bboxes:
self.seed_unique = seed_cfg['unique']
assert len(bbox
    ) == 4, 'Seed config: custom bbox {} does not have exactly four elements!'.format(
    bbox)
intersect_cfg = self.yml['tiles']['intersect']
min_x, min_y, max_x, max_y = bbox
self.intersect_expired_tiles_location = intersect_cfg['expired-location']
assert min_x < max_x, 'Invalid bbox. {} not less than {}'.format(min_x, max_x)
self.intersect_zoom_until = intersect_cfg['parent-zoom-until']
assert min_y < max_y, 'Invalid bbox. {} not less than {}'.format(min_y, max_y)
self.logconfig = self._cfg('logging config')
self.redis_type = self._cfg('redis type')
self.redis_host = self._cfg('redis host')
self.redis_port = self._cfg('redis port')
self.redis_db = self._cfg('redis db')
self.redis_cache_set_key = self._cfg('redis cache-set-key')
self.statsd_host = None
if self.yml.get('statsd'):
self.statsd_host = self._cfg('statsd host')
process_cfg = self.yml['process']
self.statsd_port = self._cfg('statsd port')
self.n_simultaneous_query_sets = process_cfg['n-simultaneous-query-sets']
self.statsd_prefix = self._cfg('statsd prefix')
self.n_simultaneous_s3_storage = process_cfg['n-simultaneous-s3-storage']
self.log_queue_sizes = process_cfg['log-queue-sizes']
self.log_queue_sizes_interval_seconds = process_cfg[
    'log-queue-sizes-interval-seconds']
self.query_cfg = process_cfg['query-config']
self.template_path = process_cfg['template-path']
self.reload_templates = process_cfg['reload-templates']
self.output_formats = process_cfg['formats']
self.buffer_cfg = process_cfg['buffer']
self.process_yaml_cfg = process_cfg['yaml']
self.postgresql_conn_info = self.yml['postgresql']
dbnames = self.postgresql_conn_info.get('dbnames')
assert dbnames is not None, 'Missing postgresql dbnames'
assert isinstance(dbnames, (tuple, list)
    ), "Expecting postgresql 'dbnames' to be a list"
assert len(dbnames) > 0, 'No postgresql dbnames configured'
self.wof = self.yml.get('wof')
self.metatile_size = self._cfg('metatile size')
self.metatile_zoom = metatile_zoom_from_size(self.metatile_size)
self.metatile_start_zoom = self._cfg('metatile start-zoom')
self.max_zoom_with_changes = self._cfg('tiles max-zoom-with-changes')
assert self.max_zoom_with_changes > self.metatile_zoom
self.max_zoom = self.max_zoom_with_changes - self.metatile_zoom
self.sql_queue_buffer_size = self._cfg('queue_buffer_size sql')
self.proc_queue_buffer_size = self._cfg('queue_buffer_size proc')
self.s3_queue_buffer_size = self._cfg('queue_buffer_size s3')
self.tile_traffic_log_path = self._cfg('toi-prune tile-traffic-log-path')
self.group_by_zoom = self.subtree('rawr group-zoom')
