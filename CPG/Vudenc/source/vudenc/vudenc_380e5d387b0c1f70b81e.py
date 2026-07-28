@app.before_request...
g.user = None
if 'username' in session:
g.user = session['username']
