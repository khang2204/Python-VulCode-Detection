@api.representation('application/json')...
"""docstring"""
if code == 204:
resp = make_response('', code)
resp = make_response(jsonify(data), code)
resp.headers.extend(headers)
return resp
