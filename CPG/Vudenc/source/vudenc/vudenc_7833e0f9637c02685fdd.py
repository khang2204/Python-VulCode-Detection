def _abort(self, job_id, message):...
"""docstring"""
self._logger.error('Error with job %d: %s', job_id, message)
self.put('worker/%s' % job_id, data={'log': message, 'returncode': 1,
    'host': socket.gethostbyaddr(socket.getfqdn())})
self._logger.exception('Error trying to PUT back abort message')
