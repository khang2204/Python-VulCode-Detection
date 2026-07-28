def genDT(endpoint, params, method):...
scope = {'class': DT, 'results': {start_url: [{'endpoint': endpoint,
    'params': params, 'method': method}]}}
script = ''
if method == 'GET':
script = createGetScript(endpoint, params)
return scope, script
