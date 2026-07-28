from pyramid.httpexceptions import HTTPFound, HTTPNoContent
from pyramid.request import Request
from pyramid.security import Allow
from pyramid.view import view_config
from . import db
from .app import RootContextFactory
from .embed import embeddable
def __getitem__(self, note_id):...
note = db.note.find_note(self.request.db, note_id)
if note:
return NoteResource(note)
def __init__(self, note: db.note.Note):...
self.note = note
@property...
return [(Allow, self.note.user_id, ('view', 'edit'))]
