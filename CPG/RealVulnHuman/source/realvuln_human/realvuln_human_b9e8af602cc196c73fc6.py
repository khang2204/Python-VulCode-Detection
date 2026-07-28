return redirect(url_for('login'))

if request.method == 'POST':
    if 'file' not in request.files:
        flash('No file part', 'error')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file', 'error')
        return redirect(request.url)
    if file:
        filename = file.filename
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Get user_id from the session username
        with get_db_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT id FROM users WHERE username = ?"
            cursor.execute(query, (session['username'],))
            user = cursor.fetchone()
            user_id = user['id']

        # Insert the file into the files table
