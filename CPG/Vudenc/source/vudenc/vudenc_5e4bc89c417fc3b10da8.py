def _execute_interactive(self, command, job_id):...
thread = threading.Thread(target=self.__execute_interactive, kwargs={
    'command': command, 'job_id': job_id})
thread.daemon = True
thread.start()
