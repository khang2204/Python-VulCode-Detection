@app.route('/email/unsubscribe/', defaults={'email': None}, methods=['GET',...
show_form = True
if not request.form.get('email') == None:
email = request.form.get('email')
if email == None:
msg = 'You need to enter your email address to unsubscribe'
results = User.query.filter_by(email=email)
return render_template('unsubscribe.html', msg=msg, show_form=show_form)
if results.count() != 1:
msg = 'The given email address was not in our system'
show_form = False
results.first().subscribed = False
db.session.commit()
msg = "We'll  stop  pestering you at " + email
