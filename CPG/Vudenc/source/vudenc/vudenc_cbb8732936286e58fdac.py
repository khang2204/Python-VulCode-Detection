@app.route('/level-2')...
if int(current_user.progress) >= 2:
return render_template('ui.html', level='2', page='index', level_progress=
    current_user.level2_progress, max_level_progress=4)
return redirect(url_prefix)
