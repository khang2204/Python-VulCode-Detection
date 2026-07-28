def update_username(self, username: str):...
"""docstring"""
self.username = username
db.session.commit()
