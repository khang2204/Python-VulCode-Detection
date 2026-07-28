@bp.route('/password-reset/<payload>', methods=['GET', 'POST'])...
if not app.config['ALLOW_PASSWORD_RESET']:
return flask.abort(404)
if flask.g.user:
return flask.redirect(redirect_url())
if payload is None:
form = forms.PasswordResetRequestForm(flask.request.form)
s = get_serializer()
if flask.request.method == 'POST' and form.validate():
request_timestamp, pw_hash, user_id = s.loads(payload)
return flask.abort(404)
user = models.User.by_id(user_id)
user = models.User.by_email(form.email.data.strip())
return flask.render_template('password_reset_request.html', form=form)
if not user:
if user:
return flask.abort(404)
if time.time() - request_timestamp > 6 * 3600:
send_password_reset_request_email(user)
flask.flash(flask.Markup(
    'A password reset request was sent to the provided email, if a matching account was found.'
    ), 'info')
return flask.abort(404)
sha1_password_hash_hash = binascii.hexlify(sha1_hash(user.password_hash.hash)
    ).decode()
return flask.redirect(flask.url_for('main.home'))
if pw_hash != sha1_password_hash_hash:
return flask.abort(404)
form = forms.PasswordResetForm(flask.request.form)
if flask.request.method == 'POST' and form.validate():
user.password_hash = form.password.data
return flask.render_template('password_reset.html', form=form)
db.session.add(user)
db.session.commit()
send_password_reset_email(user)
flask.flash(flask.Markup('Your password was reset. Log in now.'), 'info')
return flask.redirect(flask.url_for('account.login'))
