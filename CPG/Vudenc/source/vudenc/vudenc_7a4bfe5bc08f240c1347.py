@app.route('/people/new/')...
if not current_user.editor:
return redirect(url_for('error403'))
form = NameForm()
return render_template('/people/new.html', form=form)
