@bp.route('/promote/<int:id>')...
db = get_db()
user = get_user(id)
error = None
if user['restricted'] == 1:
error = 'Cannot promote restricted user.'
if user['admin'] == 1:
if error is None:
error = 'User is already an admin.'
db.execute('UPDATE user SET admin = 1 WHERE id = ?', (id,))
flash(error)
db.commit()
return redirect(url_for('admin.user_view'))
return redirect(url_for('admin.user_view'))
