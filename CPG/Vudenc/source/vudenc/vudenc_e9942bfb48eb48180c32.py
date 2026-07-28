async def post(self) ->None:...
lexer = self.get_body_argument('lexer')
raw = self.get_body_argument('code')
expiry = self.get_body_argument('expiry')
if lexer not in utility.list_languages():
log.info('Paste.post: a paste was submitted with an invalid lexer')
if not raw:
return self.redirect(f'/+{lexer}')
if expiry not in utility.expiries:
log.info('Paste.post: a paste was submitted with an invalid expiry')
paste = database.Paste(raw, lexer, utility.expiries[expiry])
session.add(paste)
session.commit()
self.set_cookie('removal', str(paste.removal_id), path=
    f'/show/{paste.paste_id}')
self.redirect(f'/show/{paste.paste_id}')
