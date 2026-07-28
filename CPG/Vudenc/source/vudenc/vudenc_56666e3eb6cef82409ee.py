@app.route('/people/<user_id>/delete_name/<name_id>', methods=['POST'])...
if not current_user.editor:
return redirect(url_for('error403'))
name_to_delete = Name.query.filter_by(id=name_id).first()
db.session.delete(name_to_delete)
db.session.commit()
return redirect(url_for('person_edit', user_id=user_id))
