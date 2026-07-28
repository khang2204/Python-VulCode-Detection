@auth.route('/oauthorize')...
resp = twitter.authorized_response()
if not resp:
flash(u'You denied the request to sign in.')
user_id = resp['user_id']
return redirect(url_for('gallery.show_posts'))
user = User.query.filter_by(user_id=user_id).first()
if user:
login_user(user)
session['user_id'] = user_id
next = request.args.get('next')
session['token'] = resp['oauth_token']
flash('You were signed in as %s' % user.username)
session['secret'] = resp['oauth_token_secret']
return redirect(url_for('auth.test'))
return redirect(url_for('auth.signup'))
