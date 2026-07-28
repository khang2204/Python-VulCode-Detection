@app.route('/level-3')...
if int(current_user.progress) >= 3:
return render_template('ui.html', level='3', page='index', level_progress=
    current_user.level3_progress, max_level_progress=3)
return redirect(url_prefix)
