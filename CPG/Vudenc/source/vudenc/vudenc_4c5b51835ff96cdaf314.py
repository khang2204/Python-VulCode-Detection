async def post(self) ->None:...
paste = await as_future(session.query(database.Paste).filter(database.Paste
    .removal_id == self.get_body_argument('removal_id')).first)
if not paste:
self.set_status(400)
session.delete(paste)
return
session.commit()
self.set_header('Content-Type', 'application/json')
self.write(json.dumps([{'paste_id': paste.paste_id, 'status': 'removed'}]))
