@view_config(route_name='note-action', request_method=('GET', 'POST'),...
"""docstring"""
db.note.delete_note(request.db, request.params['id'])
return HTTPNoContent()
