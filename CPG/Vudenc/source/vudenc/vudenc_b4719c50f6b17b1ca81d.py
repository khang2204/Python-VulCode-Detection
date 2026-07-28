@view_config(route_name='notes', permission='view', renderer=...
search = request.params.get('search', '')
from_date = request.params.get('from', '')
to_date = request.params.get('to', '')
notes = db.note.find_notes(request.db, user_id=request.user.user_id,
    from_date=from_date, to_date=to_date, search=search)
return {'notes': notes, 'from': from_date, 'to': to_date, 'search': search}
