def verify(self, data):...
credentials = self._formatCredentials(data, name='current')
command = '{} rclone lsjson current:'.format(credentials)
result = self._execute(command)
returncode = e.returncode
return {'result': True, 'message': 'Success'}
return {'result': False, 'message': 'Exit status {}'.format(returncode)}
