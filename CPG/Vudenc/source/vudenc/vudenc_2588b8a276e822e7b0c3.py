from sqlalchemy.sql import text
from .dbhelper import engine
def __init__(self, user_id, username, hashed_password, roll_id=1, *args, **...
self.user_id = user_id
self.username = username
self.hashed_password = hashed_password
self.roll_id = roll_id
def to_dict(self):...
return {'user_id': self.user_id, 'username': self.username}
