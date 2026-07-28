@bp.route('/strip/<int:id>')...
db = get_db()
user = get_user(id)
error = None
if user['admin'] != 1:
error = 'User has no admin rights.'
if error is None:
db.execute('UPDATE user SET admin = 0 WHERE id = ?', (id,))
flash(error)
db.commit()
return redirect(url_for('admin.user_view'))
return redirect(url_for('admin.user_view'))
