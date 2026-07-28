def clear_session(self):...
logging.info('Clearing flask session')
session['user'] = {}
session.clear()
