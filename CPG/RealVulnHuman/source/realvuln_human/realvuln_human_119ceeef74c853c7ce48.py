private=form.private.data,
                        user_id=current_user.id)
            session.add(note)
            session.commit()

        flash('Note created', 'success')

    return redirect('/home')


@app.route('/notes/<int:note_id>/delete', methods=['POST'])
@login_required
def delete_note(note_id: int):

    with Session() as session:
        note = session.get(Note, note_id)
        if note is None:
            flash('Note not found', 'warning')
        else:
            session.delete(note)
            session.commit()

    flash('Note deleted', 'info')
    return redirect('/home')
