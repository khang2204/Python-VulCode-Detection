from collections import defaultdict
import functools
import json
import logging
import re
import subprocess
import threading
import time
def __init__(self):...
self._job_status = defaultdict(functools.partial(defaultdict, str))
self._job_text = defaultdict(str)
self._job_error_text = defaultdict(str)
self._job_percent = defaultdict(int)
self._job_exitstatus = {}
self._stop_events = {}
self._latest_job_id = 0
def verify(self, data):...
credentials = self._formatCredentials(data, name='current')
command = '{} rclone lsjson current:'.format(credentials)
result = self._execute(command)
returncode = e.returncode
def ls(self, data, path):...
return {'result': True, 'message': 'Success'}
return {'result': False, 'message': 'Exit status {}'.format(returncode)}
credentials = self._formatCredentials(data, name='current')
command = '{credentials} rclone lsjson current:{path}'.format(credentials=
    credentials, path=path)
result = self._execute(command)
def mkdir(self, data, path):...
result = json.loads(result)
credentials = self._formatCredentials(data, name='current')
return result
command = '{credentials} rclone touch current:{path}/.keep'.format(credentials
    =credentials, path=path)
result = self._execute(command)
def copy(self, src_data, src_path, dst_data, dst_path, job_id=None):...
return {'message': 'Success'}
credentials = ''
if src_data is None:
src = src_path
credentials += self._formatCredentials(src_data, name='src')
if dst_data is None:
src = 'src:{}'.format(src_path)
dst = dst_path
credentials += self._formatCredentials(dst_data, name='dst')
command = ('{credentials} rclone copy {src} {dst} --progress --stats 2s '.
    format(credentials=credentials, src=src, dst=dst))
dst = 'dst:{}'.format(dst_path)
logging.info(sanitize(command))
if job_id is None:
job_id = self._get_next_job_id()
if self._job_id_exists(job_id):
self._stop_events[job_id] = threading.Event()
self._execute_interactive(command, job_id)
return job_id
