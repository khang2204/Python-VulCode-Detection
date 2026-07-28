def __getitem__(self, note_id):...
note = db.note.find_note(self.request.db, note_id)
if note:
return NoteResource(note)
