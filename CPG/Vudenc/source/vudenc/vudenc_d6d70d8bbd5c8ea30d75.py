def includeme(config):...
config.add_route('notes', '/notes', factory=NotesFactory)
config.add_route('new-note', '/notes/new')
config.add_route('note', pattern='/notes/{note}', traverse='/{note}',
    factory=NotesFactory)
config.add_route('note-action', '/api/notes')
