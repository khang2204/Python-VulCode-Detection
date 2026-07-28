def api_response(state, message, code):...
"""docstring"""
response = {state: message, 'status_code': code}
resp_json = jsonify(message)
return resp_json
