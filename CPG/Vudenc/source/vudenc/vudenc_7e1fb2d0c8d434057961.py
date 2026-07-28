def set_user_role(self, role: UserRole):...
"""docstring"""
self.role = role.value
db.session.commit()
