@bp.route('/unrestrict/<int:id>')...
db = get_db()
user = get_user(id)
error = None
if user['restricted'] != 1:
error = 'User already unrestricted.'
if error is None:
db.execute('UPDATE user SET restricted = 0 WHERE id = ?', (id,))
flash(error)
db.commit()
return redirect(url_for('admin.user_view'))
return redirect(url_for('admin.user_view'))
