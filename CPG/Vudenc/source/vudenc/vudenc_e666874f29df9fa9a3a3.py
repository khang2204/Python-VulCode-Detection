def _addCredential(credentials, env_key, data_key):...
value = getattr(data, data_key, None)
if value is not None:
credentials += "{}='{}' ".format(env_key, value)
return credentials
