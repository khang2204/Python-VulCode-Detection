def set_language(self, lang):...
"""docstring"""
log.debug('Updating info about user %s language in memory & database...', self)
self.language = lang
query = (
    f"UPDATE users SET language='{self.language}' WHERE chat_id='{self.chat_id}'"
    )
db.add(query)
log.error("Can't add new language of %s to the database", self)
log.debug('Language updated.')
