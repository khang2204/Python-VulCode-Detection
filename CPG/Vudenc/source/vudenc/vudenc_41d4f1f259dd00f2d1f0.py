@app.route('/screenshot/<folder>/<page>')...
if current_user.email == 'brocksmith225@gmail.com':
return render_template(folder + '/' + page + '.html')
return redirect(url_prefix)
