def validate_api_call(schema, raw_request, raw_response):...
"""docstring"""
request = normalize_request(raw_request)
validate_request(request=request, schema=schema)
errors['request'].add_error(err.messages or getattr(err, 'detail'))
response = normalize_response(raw_response, raw_request)
return
validate_response(response=response, request_method=request.method, schema=
    schema)
errors['response'].add_error(err.messages or getattr(err, 'detail'))
