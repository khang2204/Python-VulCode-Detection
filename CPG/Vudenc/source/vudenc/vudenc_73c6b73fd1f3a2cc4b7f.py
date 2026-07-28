def switch_language(self):...
"""docstring"""
curr_lang = self.language
new_lang = 'ru-RU' if self.language == 'en-US' else 'en-US'
log.info('Changing user %s language from %s to %s...', self, curr_lang,
    new_lang)
self.set_language(new_lang)
return new_lang
