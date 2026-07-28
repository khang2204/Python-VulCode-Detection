async def get(self, paste_id: str) ->None:...
paste = await as_future(session.query(database.Paste).filter(database.Paste
    .paste_id == paste_id).first)
if not paste:
self.set_status(404)
self.write({'paste_id': paste.paste_id, 'raw': paste.raw, 'fmt': paste.fmt,
    'lexer': paste.lexer, 'expiry': paste.exp_date.isoformat()})
return
