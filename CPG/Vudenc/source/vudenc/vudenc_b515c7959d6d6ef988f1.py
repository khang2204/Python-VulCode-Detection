@app.route('/level-1/create-account', methods=['POST'])...
pwd = request.form['password']
account = request.form['account']
user = BMailUser(account=account, pwd=pwd)
db_user = BMailUser.query.get(account)
if db_user:
return redirect(url_prefix + 'level-1/index')
db.session.add(user)
db.session.commit()
if int(current_user.level1_progress) <= 0:
current_user.level1_progress = 1
return redirect(url_prefix + 'level-1/inbox?account=' + user.account)
db.session.commit()
