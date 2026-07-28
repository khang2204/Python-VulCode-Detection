# Get user_id from the session username
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT id FROM users WHERE username = ?"
        cursor.execute(query, (session['username'],))
        user = cursor.fetchone()

    return render_template('edit_profile.html', user=user)

@app.route('/update_profile', methods=['POST'])
def update_profile():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    # Get current user info
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        current_user = cursor.fetchone()

    # Get form data
    new_username = request.form['username'] or current_user['username']
    email = request.form['email'] or current_user['email']
    country = request.form['country'] or current_user['country']
    if 'role' not in request.form:
        role = current_user['role']
    else:
        role = request.form['role'] or current_user['role']
    #role = request.form['role'] or current_user['role']
    #permissions = request.form['permissions'] or current_user['permissions']
    if 'permissions' not in request.form:
        permissions = current_user['permissions']
    else:
        permissions = request.form['permissions']
    team = request.form['team'] or current_user['team']

    # Handle profile picture upload
    profile_picture_id = current_user['profile_picture']
    if 'profile_picture' in request.files:
        file = request.files['profile_picture']
        if file:
            # Generate simple incremental ID for profile picture
            # Get the highest existing ID and increment it by 1
            cursor.execute("SELECT MAX(profile_picture) FROM users")
            max_id = cursor.fetchone()[0]
            if max_id is None:
                max_id = 0
            if max_id:
                profile_picture_id = max_id + 1
            else:
                profile_picture_id = 1

            # Save profile picture with simple ID
            filename = str(profile_picture_id) + '.png'
            file.save(os.path.join(PROFILE_PICTURES_UPLOAD_FOLDER, filename))

            #filename = file.filename
            #file.save(os.path.join(PROFILE_PICTURES_UPLOAD_FOLDER, filename))
            #profile_picture = filename
        else:
            profile_picture_id = current_user['profile_picture']

    # Update the user in the database
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            query = """
                UPDATE users
                SET username = ?, email = ?, country = ?, role = ?, permissions = ?, team = ?, profile_picture = ?
                WHERE username = ?
            """
            cursor.execute(query, (new_username, email, country, role, permissions, team, profile_picture_id, username))
            conn.commit()

        session['username'] = new_username  # Update session username if changed
        flash('Profile updated successfully.', 'success')
        return redirect(url_for('profile'))
    except conn.Error as e:
        print("SQLite error:", e)
        # Rollback the transaction
        conn.rollback()
        flash('Fail to update profile.', 'error')
        return redirect(url_for('edit_profile'))

# Handles file uploads
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part', 'error')
