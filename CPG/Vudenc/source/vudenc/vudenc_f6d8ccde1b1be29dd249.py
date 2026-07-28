@app.route('/issues/new/', methods=['GET', 'POST'])...
if request.method == 'GET':
form = IssueForm()
if not current_user.editor:
return render_template('/issues/new.html', form=form)
return redirect(url_for('error401'))
form = IssueForm(request.form)
if not form.validate():
return render_template('issues/new.html', form=form)
issue = Issue(form.name.data)
db.session.add(issue)
db.session.commit()
return redirect(url_for('issues_index'))
