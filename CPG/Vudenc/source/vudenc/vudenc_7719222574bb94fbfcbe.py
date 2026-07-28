@app.route('/getSession')...
if 'username' in session:
return session['user']
return 'No Session avalibale!'
