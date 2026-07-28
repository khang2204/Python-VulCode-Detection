@app.before_request...
if request.method == 'POST':
token = session.pop('_csrf_token', None)
if not token or token != request.form.get('_csrf_token'):
abort(403)
session['_csrf_token'] = generate_csrf_token()
