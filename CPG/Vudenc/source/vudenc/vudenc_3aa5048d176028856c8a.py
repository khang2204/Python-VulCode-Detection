@staticmethod...
"""docstring"""
params['url'] = data.url
params['credentials'] = json.dumps(data.credentials)
params['scopes'] = '\n'.join(data.scopes)
params['headers'] = json.dumps(data.headers)
