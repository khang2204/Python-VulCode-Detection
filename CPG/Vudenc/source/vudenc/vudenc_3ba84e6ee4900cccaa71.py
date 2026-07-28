@app.route('/people/', methods=['POST'])...
if not current_user.editor:
return redirect(url_for('error403'))
form = NameForm(request.form)
if not form.validate():
return render_template('people/new.html', form=form)
u = User(form.name.data, '', '')
db.session().add(u)
db.session().commit()
u.add_name(form.name.data)
return redirect(url_for('people_index'))
