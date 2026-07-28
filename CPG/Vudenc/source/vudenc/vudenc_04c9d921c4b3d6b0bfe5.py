@app.route('/video/<filename>')...
if 'username' in session:
return render_template('video_viewing_screen.html', video_name=filename)
return redirect(url_for('index'))
