def update_log_filenames(self):...
"""docstring"""
num_current_log_files = len(self.log_files)
new_log_filenames = self.redis_client.lrange('LOG_FILENAMES:{}'.format(self
    .node_ip_address), num_current_log_files, -1)
for log_filename in new_log_filenames:
logger.info('Beginning to track file {}'.format(log_filename))
assert log_filename not in self.log_files
self.log_files[log_filename] = []
