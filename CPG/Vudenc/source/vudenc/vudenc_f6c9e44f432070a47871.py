async def get(self, paste_id: str) ->None:...
paste = await as_future(session.query(database.Paste).filter(database.Paste
    .paste_id == paste_id).first)
if not paste:
self.set_status(404)
can_delete = self.get_cookie('removal') == str(paste.removal_id)
self.render('404.html', pagetitle='404')
self.render('show.html', paste=paste, pagetitle='show', can_delete=
    can_delete, linenos=False)
return
