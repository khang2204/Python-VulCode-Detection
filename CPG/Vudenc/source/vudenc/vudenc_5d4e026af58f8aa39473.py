def createPostScript(endpoint, params):...
keys = params.keys()
values = params.values()
pair = [(keys[i] + '=' + values[i]) for i in range(len(keys))]
evil_param = '&'.join(pair)
script = ('curl -d ' + '"' + evil_param + '" ' + '-X POST ' + start_url +
    endpoint)
return script
