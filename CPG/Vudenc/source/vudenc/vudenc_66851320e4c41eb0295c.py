def __init__(self, db_path):...
"""docstring"""
self.connection = False
self.db_path = db_path
if os.path.exists(self.db_path) and os.path.isfile(self.db_path):
self.connection = sqlite3.connect(self.db_path)
print('db does not exist')
self.cursor = self.connection.cursor()
