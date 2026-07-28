personal_notes = session.query(Note).filter(
            Note.user_id == current_user.id,
            text(f"text like '%{search_param}%'")).all()
        return render_template(
            'search.html',
            search=search_param,
            personal_notes=personal_notes,
        )


@app.route('/accounts/<int:user_id>/notes')
@login_required
def get_personal_notes(user_id: int):
    with Session() as session:
        personal_notes = session.query(Note).filter(
            Note.user_id == user_id).all()
        return render_template('personal_notes.html',
                               personal_notes=personal_notes)


@app.route('/account/image', methods=['POST'])
@login_required
def add_image():
    form = ImageForm(request.form)

    if not form.validate():
        flash(json.dumps(form.errors), 'error')
    else:
