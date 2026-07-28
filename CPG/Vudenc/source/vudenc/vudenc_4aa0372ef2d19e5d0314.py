def is_expired(self):...
if 'expiration' in session:
if session.get('max_expiration') is None:
return False
logging.warning('max_expiration unset on session, when expiration is set.')
now = datetime.datetime.utcnow()
return True
if now > session['expiration']:
return True
if now > session['max_expiration']:
return True
