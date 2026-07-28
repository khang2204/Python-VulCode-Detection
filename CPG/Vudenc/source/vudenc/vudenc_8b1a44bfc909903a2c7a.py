async def get(self, removal_id: str) ->None:...
"""docstring"""
paste = await as_future(session.query(database.Paste).filter(database.Paste
    .removal_id == removal_id).first)
if not paste:
log.info('RemovePaste.get: someone visited with invalid id')
session.delete(paste)
self.set_status(404)
session.commit()
self.render('404.html', pagetitle='404')
self.redirect('/')
return
