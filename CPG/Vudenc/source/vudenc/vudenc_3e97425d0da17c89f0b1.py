def __init__(self, redis_ip_address, redis_port, node_ip_address,...
"""docstring"""
self.node_ip_address = node_ip_address
self.redis_client = redis.StrictRedis(host=redis_ip_address, port=
    redis_port, password=redis_password)
self.log_files = {}
self.log_file_handles = {}
self.files_to_ignore = set()
