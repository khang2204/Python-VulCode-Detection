@app.route('/level-4')...
if int(current_user.progress) >= 4:
return render_template('ui.html', level='4', page='index', level_progress=
    current_user.level4_progress, max_level_progress=3)
return redirect(url_prefix)
