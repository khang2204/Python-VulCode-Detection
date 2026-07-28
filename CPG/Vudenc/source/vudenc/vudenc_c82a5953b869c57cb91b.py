@wraps(func)...
result = json.dumps(func(*args, **kwargs) or {'error':
    'No data found for your request'}, default=serialize_to_json)
headers = [('Content-Type', 'application/json'), ('Content-Length', str(len
    (result)))]
return Response(result, status=200, headers=headers)
