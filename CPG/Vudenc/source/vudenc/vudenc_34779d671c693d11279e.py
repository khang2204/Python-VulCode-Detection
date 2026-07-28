def save_note(conn, note: Note) ->Note:...
if note.note_id:
cur.execute(
    'UPDATE note SET content = ?, updated_at = CURRENT_TIMESTAMP WHERE note_id = ?'
    , (note.content, note.note_id))
cur.execute('INSERT INTO note(user_id, content) VALUES(?, ?)', (note.
    user_id, note.content))
new_note = _find_note(cur, note.note_id)
note.note_id = cur.lastrowid
return new_note
