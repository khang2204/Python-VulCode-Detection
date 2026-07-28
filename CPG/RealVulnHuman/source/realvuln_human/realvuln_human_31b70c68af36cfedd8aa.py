cursor.execute(query, (session['username'],))
        user = cursor.fetchone()
        user_id = user['id']

    # Check if the file belongs to the user
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
