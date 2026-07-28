@app.route('/people/<user_id>/', methods=['GET'])...
user = User.query.get(int(user_id))
if not user:
return redirect(url_for('error404'))
name = user.name
articles_writing = user.get_articles_writing()
articles_editing = user.get_articles_editing()
return render_template('people/tasks.html', articles_writing=
    articles_writing, articles_editing=articles_editing, posessive_form='' +
    name + "'s", system_name=user.name, person_is=name + ' is')
