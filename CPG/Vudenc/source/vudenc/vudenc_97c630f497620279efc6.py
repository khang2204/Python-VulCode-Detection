def _find_note(cur, note_id):...
return db.fetchone(cur, Note,
    f'SELECT note_id, user_id, content, created_at, updated_at FROM note WHERE note_id = {note_id}'
    , ())
