def validate_request(schema):...
"""docstring"""
def decorator(func):...
@wraps(func)...
def default_encode(value):...
if callable(value):
return value()
if request.method == 'POST':
return func(*args, **kwargs)
body = json.loads(request.data)
result = {'error': {'type': 'schema', 'message': str(e)}, 'schema': schema}
schemas.validate(body, schema)
return json.dumps(result, sort_keys=True, indent=4, default=default_encode
    ), 400, {'Content-Type': 'application/json'}
kwargs['validated_body'] = body
if kwargs.get('timer'):
kwargs['timer'].mark('validate_schema')
