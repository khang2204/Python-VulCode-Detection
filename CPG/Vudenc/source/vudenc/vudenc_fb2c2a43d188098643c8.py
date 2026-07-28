@bp.route('/edituser/<int:id>', methods=('GET', 'POST'))...
user = get_user(id)
if request.method == 'POST':
username = request.form['username']
return render_template('admin/edituser.html', user=user)
desc = request.form['desc']
role = request.form['role']
adminPwd = request.form['adminPwd']
db = get_db()
error = None
file = None
imgAdded = False
if 'file' in request.files:
f = request.files['file']
if not check_password_hash(g.user['password'], adminPwd):
filename = secure_filename(f.filename)
error = 'Incorrect admin password. Correct password required to edit user.'
if error is None:
filetype = filename.rsplit('.', 1)[1].lower()
if username is not '':
flash(error)
f.save(os.path.join(current_app.config['UPLOAD_FOLDER'], str(g.user['id']) +
    '.' + filetype))
db.execute('UPDATE user SET name = ? WHERE id = ?', (username, id))
if desc is not '':
imgAdded = True
db.execute('UPDATE user SET descrip = ? WHERE id = ?', (desc, id))
if imgAdded:
db.execute('UPDATE user SET avatar = 1 WHERE id = ?', (id,))
if role == 'restricted':
db.execute('UPDATE user SET restricted = 1 WHERE id = ?', (id,))
if role == 'admin':
db.execute('UPDATE user SET admin = 1 WHERE id = ?', (id,))
db.commit()
return redirect(url_for('user.show_profile', id=user['id']))
