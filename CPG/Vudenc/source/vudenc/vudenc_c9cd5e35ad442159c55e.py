def mark_as_read(self):...
"""docstring"""
self.read = True
db.session.commit()
