@bp.route('/register', methods=['GET', 'POST'])...
if flask.g.user:
return flask.redirect(redirect_url())
form = forms.RegisterForm(flask.request.form)
if flask.request.method == 'POST' and form.validate():
user = models.User(username=form.username.data.strip(), email=form.email.
    data.strip(), password=form.password.data)
return flask.render_template('register.html', form=form)
user.registration_ip = ip_address(flask.request.remote_addr).packed
user.last_login_ip = user.registration_ip
db.session.add(user)
db.session.commit()
if models.RangeBan.is_rangebanned(user.registration_ip):
flask.flash(flask.Markup(
    'Your IP is blocked from creating new accounts. Please <a href="{}">ask a moderator</a> to manually activate your account <a href="{}">\'{}\'</a>.'
    .format(flask.url_for('site.help') + '#irchelp', flask.url_for(
    'users.view_user', user_name=user.username), user.username)), 'warning')
if app.config['USE_EMAIL_VERIFICATION']:
send_verification_email(user)
user.status = models.UserStatusType.ACTIVE
return flask.render_template('waiting.html')
db.session.add(user)
db.session.commit()
flask.g.user = user
flask.session['user_id'] = user.id
flask.session.permanent = True
flask.session.modified = True
return flask.redirect(redirect_url())
