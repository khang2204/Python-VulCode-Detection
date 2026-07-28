import json
import logging
from typing import List
from datetime import timedelta
import tornado.web
from tornado_sqlalchemy import as_future, SessionMixin
from pinnwand import database
from pinnwand import utility
from pinnwand import path
log = logging.getLogger(__name__)
async def get(self) ->None:...
self.render('about.html', pagetitle='about')
"""The index page shows the new paste page with a list of all available
       lexers from Pygments."""
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
async def post(self) ->None:...
self.render('404.html', pagetitle='404')
lexer = self.get_body_argument('lexer')
return
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
def check_xsrf_cookie(self) ->bool:...
"""docstring"""
return True
