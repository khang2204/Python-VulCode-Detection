@app.route('/screenshot/<page>')...
if current_user.email == 'brocksmith225@gmail.com':
return render_template(page + '.html')
return redirect(url_prefix)
