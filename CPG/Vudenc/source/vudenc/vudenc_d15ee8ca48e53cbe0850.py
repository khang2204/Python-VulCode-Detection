def set_is_expert(self, is_expert: bool):...
"""docstring"""
self.is_expert = is_expert
db.session.commit()
