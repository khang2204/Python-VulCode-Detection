def set_email_verified_status(self, is_verified: bool):...
"""docstring"""
self.is_email_verified = is_verified
db.session.commit()
