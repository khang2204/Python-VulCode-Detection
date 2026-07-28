@app.route('/level-1/info')...
if int(current_user.progress) > 1:
return render_template('info-pages/level-1.html')
return redirect('/')
