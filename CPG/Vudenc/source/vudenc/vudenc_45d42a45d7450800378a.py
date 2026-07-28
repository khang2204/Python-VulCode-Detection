def __process_text(self, job_id):...
headers = ['GTransferred', 'Errors', 'Checks', 'Transferred',
    'Elapsed time', 'Transferring']
status = self._job_status[job_id]
text = '\n'.join('{:>12}: {}'.format(header, status[header]) for header in
    headers)
self._job_text[job_id] = text
