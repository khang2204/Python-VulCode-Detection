query = "SELECT * FROM files WHERE filename = ? AND user_id = ?"
    cursor.execute(query, (filename, user_id))
    file = cursor.fetchone()

    if file:
        return send_from_directory(UPLOAD_FOLDER, filename)
    else:
        return "Forbidden", 403

# Route to serve uploaded profile pictures
@app.route('/uploads/profile_pictures/<filename>')
def profile_pictures(filename):
    return send_from_directory(PROFILE_PICTURES_UPLOAD_FOLDER, filename)

# Route to download file
@app.route('/download/<filename>')
def download_file(filename):
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']

    # Query the database for the user ID
