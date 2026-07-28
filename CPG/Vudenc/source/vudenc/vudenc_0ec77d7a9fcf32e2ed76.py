def copy(self, src_data, src_path, dst_data, dst_path, job_id=None):...
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
