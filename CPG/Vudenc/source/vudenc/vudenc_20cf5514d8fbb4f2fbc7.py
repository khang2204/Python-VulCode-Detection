def to_database_query(self):...
data = [self.project_id, self.user_id, self.money, self.time]
data = [repr(x) for x in data]
labels = ['project_id', 'user_id', 'money', 'timestamp']
return dict(zip(labels, data))
