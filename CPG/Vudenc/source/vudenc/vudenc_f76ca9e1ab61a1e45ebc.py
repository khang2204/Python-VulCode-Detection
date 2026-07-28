def save(self):...
"""docstring"""
db.session.add(self)
db.session.commit()
