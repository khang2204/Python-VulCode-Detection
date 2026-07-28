# Get user_id from the session username
        with get_db_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT id FROM users WHERE username = ?"
            cursor.execute(query, (session['username'],))
            user = cursor.fetchone()
            user_id = user['id']

        if search_query:
            s_query = f"SELECT filename FROM files WHERE user_id = {user_id} AND filename LIKE '%{search_query}%'"
            cursor.execute(s_query)
        else:
            cursor.execute("SELECT filename FROM files WHERE user_id = ?", (user_id,))
        files = [row['filename'] for row in cursor.fetchall()]

        return render_template('dashboard.html', files=files, search_query=search_query)
    else:
        return redirect(url_for('login'))

@app.route('/profile')
def profile():
