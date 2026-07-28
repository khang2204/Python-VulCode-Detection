async def get(self, paste_id: str) ->None:...
paste = await as_future(session.query(database.Paste).filter(database.Paste
    .paste_id == paste_id).first)
if not paste:
self.set_status(404)
self.set_header('Content-Type', 'text/plain; charset=utf-8')
self.render('404.html', pagetitle='404')
self.write(paste.raw)
return
