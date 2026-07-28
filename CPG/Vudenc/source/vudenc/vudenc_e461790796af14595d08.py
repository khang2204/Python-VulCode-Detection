@bp.route('/login', methods=['GET', 'POST'])...
if flask.g.user:
return flask.redirect(redirect_url())
form = forms.LoginForm(flask.request.form)
if flask.request.method == 'POST' and form.validate():
if app.config['MAINTENANCE_MODE'] and not app.config['MAINTENANCE_MODE_LOGINS'
return flask.render_template('login.html', form=form)
flask.flash(flask.Markup('<strong>Logins are currently disabled.</strong>'),
    'danger')
username = form.username.data.strip()
return flask.redirect(flask.url_for('account.login'))
password = form.password.data
user = models.User.by_username(username)
if not user:
user = models.User.by_email(username)
if not user or password != user.password_hash:
flask.flash(flask.Markup(
    '<strong>Login failed!</strong> Incorrect username or password.'), 'danger'
    )
if user.is_banned:
return flask.redirect(flask.url_for('account.login'))
ban_reason = models.Ban.banned(user.id, None).first().reason
if user.status != models.UserStatusType.ACTIVE:
ban_str = (
    '<strong>Login failed!</strong> You are banned with the reason "{0}" If you believe that this is a mistake, contact a moderator on IRC.'
    .format(ban_reason))
flask.flash(flask.Markup(
    '<strong>Login failed!</strong> Account is not activated.'), 'danger')
user.last_login_date = datetime.utcnow()
flask.flash(flask.Markup(ban_str), 'danger')
return flask.redirect(flask.url_for('account.login'))
user.last_login_ip = ip_address(flask.request.remote_addr).packed
return flask.redirect(flask.url_for('account.login'))
if not app.config['MAINTENANCE_MODE']:
db.session.add(user)
flask.g.user = user
db.session.commit()
flask.session['user_id'] = user.id
flask.session.permanent = True
flask.session.modified = True
return flask.redirect(redirect_url())
