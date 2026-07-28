def check_log_files_and_push_updates(self):...
"""docstring"""
for log_filename in self.log_files:
if log_filename in self.log_file_handles:
new_lines = []
if log_filename in self.files_to_ignore:
while True:
self.log_file_handles[log_filename] = open(log_filename, 'r')
if e.errno == os.errno.EMFILE:
current_position = self.log_file_handles[log_filename].tell()
logger.warning('Warning: Ignoring {} because there are too many open files.'
    .format(log_filename))
if e.errno == os.errno.ENOENT:
next_line = self.log_file_handles[log_filename].readline()
self.files_to_ignore.add(log_filename)
logger.warning('Warning: The file {} was not found.'.format(log_filename))
if next_line != '':
new_lines.append(next_line)
self.log_file_handles[log_filename].seek(current_position)
if len(new_lines) > 0:
self.log_files[log_filename] += new_lines
redis_key = 'LOGFILE:{}:{}'.format(self.node_ip_address, ray.utils.decode(
    log_filename))
self.redis_client.rpush(redis_key, *new_lines)
