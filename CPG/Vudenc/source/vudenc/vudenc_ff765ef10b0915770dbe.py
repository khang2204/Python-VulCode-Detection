@app.route('/saveAs')...
if not 'email' in session and not 'social' in session:
if 'diagram' in request.args or diagram:
return render_template('saveFile.html', diagram=diagram)
return redirect('/login?return_url=saveAs&diagram=true')
return redirect('/login?return_url=saveAs')
