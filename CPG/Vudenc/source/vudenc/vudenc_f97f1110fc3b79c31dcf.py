@app.route('/level-1/login', methods=['POST'])...
user = BMailUser.query.get(request.form['account'])
if user:
if request.form['password'] == user.pwd:
return redirect(url_prefix + 'level-1/index')
if int(current_user.level1_progress) <= 1 and str(request.form['account']
current_user.level1_progress = 2
return redirect(url_prefix + 'level-1/inbox?account=' + user.account)
db.session.commit()
