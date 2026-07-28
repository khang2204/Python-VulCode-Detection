def ls(self, data, path):...
credentials = self._formatCredentials(data, name='current')
command = '{credentials} rclone lsjson current:{path}'.format(credentials=
    credentials, path=path)
result = self._execute(command)
result = json.loads(result)
return result
