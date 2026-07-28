from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import argparse
import logging
import os
import redis
import time
import ray.ray_constants as ray_constants
from ray.services import get_ip_address
from ray.services import get_port
import ray.utils
logger = logging.getLogger(__name__)
"""A monitor process for monitoring Ray log files.

    Attributes:
        node_ip_address: The IP address of the node that the log monitor
            process is running on. This will be used to determine which log
            files to track.
        redis_client: A client used to communicate with the Redis server.
        log_files: A dictionary mapping the name of a log file to a list of
            strings representing its contents.
        log_file_handles: A dictionary mapping the name of a log file to a file
            handle for that file.
    """
def __init__(self, redis_ip_address, redis_port, node_ip_address,...
"""docstring"""
self.node_ip_address = node_ip_address
self.redis_client = redis.StrictRedis(host=redis_ip_address, port=
    redis_port, password=redis_password)
self.log_files = {}
self.log_file_handles = {}
self.files_to_ignore = set()
def update_log_filenames(self):...
"""docstring"""
num_current_log_files = len(self.log_files)
new_log_filenames = self.redis_client.lrange('LOG_FILENAMES:{}'.format(self
    .node_ip_address), num_current_log_files, -1)
for log_filename in new_log_filenames:
logger.info('Beginning to track file {}'.format(log_filename))
def check_log_files_and_push_updates(self):...
assert log_filename not in self.log_files
"""docstring"""
self.log_files[log_filename] = []
for log_filename in self.log_files:
if log_filename in self.log_file_handles:
def run(self):...
new_lines = []
if log_filename in self.files_to_ignore:
"""docstring"""
while True:
self.log_file_handles[log_filename] = open(log_filename, 'r')
if e.errno == os.errno.EMFILE:
while True:
current_position = self.log_file_handles[log_filename].tell()
logger.warning('Warning: Ignoring {} because there are too many open files.'
    .format(log_filename))
if e.errno == os.errno.ENOENT:
self.update_log_filenames()
next_line = self.log_file_handles[log_filename].readline()
self.files_to_ignore.add(log_filename)
logger.warning('Warning: The file {} was not found.'.format(log_filename))
self.check_log_files_and_push_updates()
if next_line != '':
time.sleep(1)
new_lines.append(next_line)
self.log_file_handles[log_filename].seek(current_position)
if len(new_lines) > 0:
self.log_files[log_filename] += new_lines
redis_key = 'LOGFILE:{}:{}'.format(self.node_ip_address, ray.utils.decode(
    log_filename))
self.redis_client.rpush(redis_key, *new_lines)
