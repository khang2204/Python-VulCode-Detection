@app.route('/logout')...
session.clear()
if 'return_url' in request.args:
return redirect(request.args['return_url'])
return redirect('/')
