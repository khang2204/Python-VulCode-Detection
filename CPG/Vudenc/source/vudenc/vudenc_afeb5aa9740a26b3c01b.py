@app.route('/people/<user_id>/edit', methods=['GET'])...
form = NameForm()
name = ''
username = ''
prsn = User.query.filter_by(id=user_id).first()
if prsn.username != '':
username = prsn.username
name = prsn.name
names = list(map(lambda name: {'name': name.name, 'id': name.id}, prsn.names))
person = {'id': user_id, 'name': name, 'username': username, 'names': names}
return render_template('/people/edit.html', person=person, form=form)
