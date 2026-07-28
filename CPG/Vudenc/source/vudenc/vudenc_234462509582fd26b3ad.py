@app.route('/<string:filename>')...
filename = os.path.join(static_path, filename)
if os.path.exists(filename):
response_body = f.read()
abort(404)
return response_body
