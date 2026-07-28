def createGetScript(endpoint, params):...
script = 'curl ' + start_url + endpoint + '?'
keys = params.keys()
values = params.values()
pair = [(keys[i] + '=' + values[i]) for i in range(len(keys))]
evil_param = '&'.join(pair)
script += evil_param
return script
