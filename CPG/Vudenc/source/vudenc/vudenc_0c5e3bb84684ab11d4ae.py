@app.route('/level-1')...
if int(current_user.progress) >= 1:
return render_template('ui.html', level='1', page='index', level_progress=
    current_user.level1_progress, max_level_progress=3)
return redirect(url_prefix)
