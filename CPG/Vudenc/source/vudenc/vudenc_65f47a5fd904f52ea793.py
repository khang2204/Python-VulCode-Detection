@bp.route('/profile', methods=['GET', 'POST'])...
if not flask.g.user:
return flask.redirect(flask.url_for('main.home'))
form = forms.ProfileForm(flask.request.form)
if flask.request.method == 'POST' and form.validate():
user = flask.g.user
return flask.render_template('profile.html', form=form)
new_email = form.email.data.strip()
new_password = form.new_password.data
if new_email:
if form.current_password.data != user.password_hash:
if new_password:
flask.flash(flask.Markup(
    '<strong>Email change failed!</strong> Incorrect password.'), 'danger')
user.email = form.email.data
if form.current_password.data != user.password_hash:
db.session.add(user)
return flask.redirect('/profile')
flask.flash(flask.Markup('<strong>Email successfully changed!</strong>'),
    'success')
flask.flash(flask.Markup(
    '<strong>Password change failed!</strong> Incorrect password.'), 'danger')
user.password_hash = form.new_password.data
db.session.commit()
return flask.redirect('/profile')
flask.flash(flask.Markup('<strong>Password successfully changed!</strong>'),
    'success')
flask.g.user = user
return flask.redirect('/profile')
