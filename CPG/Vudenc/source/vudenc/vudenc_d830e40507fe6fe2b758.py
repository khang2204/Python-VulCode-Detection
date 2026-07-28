@bp.route('/restrict/<int:id>')...
db = get_db()
user = get_user(id)
error = None
if user['restricted'] == 1:
error = 'User already restricted.'
if user['admin'] == 1:
if error is None:
error = 'Cannot restrict admins.'
db.execute('UPDATE user SET restricted = 1 WHERE id = ?', (id,))
flash(error)
db.commit()
return redirect(url_for('admin.user_view'))
return redirect(url_for('admin.user_view'))
