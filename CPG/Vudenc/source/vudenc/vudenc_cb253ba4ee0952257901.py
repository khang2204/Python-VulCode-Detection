@app.route('/callback/<provider>')...
oauth = OAuthSignIn.get_provider(provider)
social, username, email = oauth.callback()
if social is None:
flash('Authentication failed.')
user = query_social_user(social)
return redirect(url_for('login'))
session['social'] = social
if user is None:
insert_social_user(social)
return redirect('/')
