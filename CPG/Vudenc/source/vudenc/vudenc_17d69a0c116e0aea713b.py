@bp.route('/delete/<int:id>')...
db = get_db()
db.execute('DELETE FROM user WHERE id = ?', (id,))
db.commit()
message = 'Deleted user!'
flash(message)
return redirect(url_for('admin.user_view'))
