def set_expiration(self):...
if app.config['PERMANENT_SESSION_LIFETIME']:
session.permanent = True
now = datetime.datetime.utcnow()
lifetime = app.config['PERMANENT_SESSION_LIFETIME']
expiration = now + datetime.timedelta(seconds=lifetime)
session['expiration'] = expiration
if not session.get('max_expiration'):
max_lifetime = app.config['MAX_PERMANENT_SESSION_LIFETIME']
if not max_lifetime:
max_lifetime = lifetime
max_expiration = now + datetime.timedelta(seconds=max_lifetime)
session['max_expiration'] = max_expiration
