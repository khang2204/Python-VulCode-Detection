@bp.route('post/delete/<int:pid>')...
db = get_db()
db.execute('DELETE FROM post WHERE pid = ?', (pid,))
db.commit()
message = 'Deleted post!'
flash(message)
return redirect(url_for('admin.admin_panel'))
