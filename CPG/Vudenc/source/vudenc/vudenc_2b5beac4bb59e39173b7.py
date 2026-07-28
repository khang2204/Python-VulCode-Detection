def _formatCredentials(self, data, name):...
"""docstring"""
prefix = 'RCLONE_CONFIG_{}'.format(name.upper())
credentials = ''
credentials += "{}_TYPE='{}' ".format(prefix, data.type)
def _addCredential(credentials, env_key, data_key):...
value = getattr(data, data_key, None)
if value is not None:
credentials += "{}='{}' ".format(env_key, value)
return credentials
