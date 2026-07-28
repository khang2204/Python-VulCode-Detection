def _save_or_create_note(note: db.note.Note, request: Request):...
content: str = request.params['note']
note.content = content.replace('\r', '')
return db.note.save_note(request.db, note)
