@view_config(route_name='new-note', permission='edit', renderer=...
note = db.note.Note(None, user_id=request.user.user_id, content=request.
    params.get('note', ''))
if request.method == 'POST':
_save_or_create_note(note, request)
return dict(title='Ny anteckning', note=note)
return HTTPFound(location=request.route_url('notes'))
