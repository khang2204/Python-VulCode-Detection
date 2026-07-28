@app.route('/signup')...
if 'return_url' in request.args:
session['return_url'] = request.args['return_url']
return render_template('register.html')
