def _get_next_job_id(self):...
self._latest_job_id += 1
while self._job_id_exists(self._latest_job_id):
self._latest_job_id += 1
return self._latest_job_id
