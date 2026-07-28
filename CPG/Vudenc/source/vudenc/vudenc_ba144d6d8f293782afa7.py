async def get(self, lexer: str='') ->None:...
"""docstring"""
lexers = utility.list_languages()
if not lexer:
lexer = 'text'
if lexer not in lexers:
log.debug('CreatePaste.get: non-existent logger requested')
await self.render('new.html', lexer=lexer, lexers=lexers, pagetitle='new',
    message=None)
self.set_status(404)
self.render('404.html', pagetitle='404')
return
