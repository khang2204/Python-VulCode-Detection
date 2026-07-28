import datetime
import MySQLdb
from backend.SQLConnector import SQLConnector
TABLE_NAME = 'transactions'
def __init__(self, project_id, user_id, money):...
self.project_id = project_id
self.user_id = user_id
self.money = money
self.time = datetime.datetime.now().isoformat(' ')
def to_json_obj(self):...
obj = {'id': self.id, 'project_id': self.project_id, 'user_id': self.
    user_id, 'money': self.money, 'time': self.time}
return obj
