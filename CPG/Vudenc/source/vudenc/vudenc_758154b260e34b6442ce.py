@app.route('/manage')...
if current_user.is_authenticated:
return render_template('manage.html')
return redirect('/index')
