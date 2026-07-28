async def post(self) ->None:...
lexer = self.get_body_argument('lexer')
raw = self.get_body_argument('code')
expiry = self.get_body_argument('expiry')
if not raw:
log.info('APINew.post: a paste was submitted without content')
if lexer not in utility.list_languages():
log.info('APINew.post: a paste was submitted with an invalid lexer')
if expiry not in utility.expiries:
log.info('APINew.post: a paste was submitted with an invalid expiry')
paste = database.Paste(raw, lexer, utility.expiries[expiry])
session.add(paste)
session.commit()
self.write({'paste_id': paste.paste_id, 'removal_id': paste.removal_id})
