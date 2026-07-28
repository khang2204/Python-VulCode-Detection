def add_store(self, store):...
"""docstring"""
t = store[0],
self.cursor.execute('insert into store (name) values (?)', t)
self.connection.commit()
