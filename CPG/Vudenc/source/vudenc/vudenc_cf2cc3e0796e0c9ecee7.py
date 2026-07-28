@auth.route('/signup', methods=['GET', 'POST'])...
form = RegistrationForm()
if request.method == 'POST' and form.validate_on_submit():
username = ''.join([form.adj.data, form.benwa.data, form.pos.data])
flash('There was an issue with sign up, please try again')
name_exists = User.query.filter(User.username == username).all()
return render_template('signup.html', form=form)
if name_exists:
flash('Username %s already in use' % username)
user = user_datastore.create_user(user_id=session['user_id'], username=username
    )
return redirect(url_for('auth.signup'))
user.oauth_token = session.pop('token')
user.oauth_secret = session.pop('secret')
db.session.commit()
login_user(user)
next = request.args.get('next')
flash('You were signed in as %s' % user.username)
return redirect(url_for('auth.test'))
