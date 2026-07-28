@app.route('/search')
@login_required
def search():
    search_param = request.args.get('search', '')
    with Session() as session:
        session.query(Note)

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
