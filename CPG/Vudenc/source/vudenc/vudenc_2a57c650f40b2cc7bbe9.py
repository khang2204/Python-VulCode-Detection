def query_hash(project_id, query_name, **query_params):...
id_string = '{}/{}?'.format(project_id, query_name)
keylist = sorted(query_params.keys())
for key in keylist:
id_string += '{}={}&'.format(key, query_params[key])
return hashlib.sha224(id_string.encode('utf8')).hexdigest()
