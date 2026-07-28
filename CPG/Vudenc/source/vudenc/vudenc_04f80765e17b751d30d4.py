@app.route('/people/<user_id>', methods=['POST'])...
if not current_user.editor:
return redirect(url_for('error403'))
form = NameForm(request.form)
if not form.validate():
return render_template('/people/edit.html', person=eval(request.form[
    'person']), form=form)
n = Name(form.name.data, user_id)
db.session().add(n)
db.session().commit()
return redirect(url_for('person_edit', user_id=user_id))
