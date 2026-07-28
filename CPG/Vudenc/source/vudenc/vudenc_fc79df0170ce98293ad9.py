def default_yml_config():...
return {'queue': {'name': None, 'type': 'sqs', 'timeout-seconds': 20},
    'store': {'type': 's3', 'name': None, 'path': 'osm',
    'reduced-redundancy': False, 'date-prefix': '', 'delete-retry-interval':
    60}, 'aws': {'credentials': {'aws_access_key_id': None,
    'aws_secret_access_key': None}}, 'tiles': {'seed': {'all': {
    'zoom-start': None, 'zoom-until': None}, 'metro-extract': {'url': None,
    'zoom-start': None, 'zoom-until': None, 'cities': None}, 'top-tiles': {
    'url': None, 'zoom-start': None, 'zoom-until': None}, 'custom': {
    'zoom-start': None, 'zoom-until': None, 'bboxes': []},
    'should-add-to-tiles-of-interest': True, 'n-threads': 50, 'unique': 
    True}, 'intersect': {'expired-location': None, 'parent-zoom-until':
    None}, 'max-zoom-with-changes': 16}, 'toi-store': {'type': None},
    'toi-prune': {'tile-traffic-log-path': '/tmp/tile-traffic.log'},
    'process': {'n-simultaneous-query-sets': 0, 'n-simultaneous-s3-storage':
    0, 'log-queue-sizes': True, 'log-queue-sizes-interval-seconds': 10,
    'query-config': None, 'template-path': None, 'reload-templates': False,
    'formats': ['json'], 'buffer': {}, 'yaml': {'type': None, 'parse': {
    'path': ''}, 'callable': {'dotted-name': ''}}}, 'logging': {'config':
    None}, 'redis': {'host': 'localhost', 'port': 6379, 'db': 0,
    'cache-set-key': 'tilequeue.tiles-of-interest', 'type': 'redis_client'},
    'postgresql': {'host': 'localhost', 'port': 5432, 'dbnames': ('osm',),
    'user': 'osm', 'password': None}, 'metatile': {'size': None,
    'start-zoom': 0}, 'queue_buffer_size': {'sql': None, 'proc': None, 's3':
    None}}
