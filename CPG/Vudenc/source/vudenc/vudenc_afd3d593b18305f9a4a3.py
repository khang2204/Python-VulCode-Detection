def __process_percent(self, job_id):...
status = self._job_status[job_id]
match = re.search('(\\d+)\\%', status['GTransferred'])
if match is None:
self._job_percent[job_id] = -1
self._job_percent[job_id] = match[1]
