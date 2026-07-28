@bp.route('post/release/<int:pid>')...
db = get_db()
db.execute('UPDATE post SET reviewed = 0 WHERE pid = ?', (pid,))
db.commit()
message = 'Released post!'
flash(message)
return redirect(url_for('admin.admin_panel'))
