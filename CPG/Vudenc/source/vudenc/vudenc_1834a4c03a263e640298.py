def genSI(endpoint, params, method):...
scope = {'class': SI, 'results': {start_url: [{'endpoint': endpoint,
    'params': params, 'method': method}]}}
if method == 'POST':
script = createPostScript(endpoint, params)
return scope, script
