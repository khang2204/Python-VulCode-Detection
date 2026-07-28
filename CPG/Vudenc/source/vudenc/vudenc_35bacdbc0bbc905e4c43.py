def add_language(self, language):...
"""docstring"""
if self.connection:
self.cursor.execute('insert into itemlanguage (language) values ("%s")' %
    language[0])
self.connection.commit()
