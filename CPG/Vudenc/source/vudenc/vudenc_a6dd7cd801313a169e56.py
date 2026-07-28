def add_message(self):...
"""docstring"""
current_app.logger.debug('Adding message to session')
db.session.add(self)
