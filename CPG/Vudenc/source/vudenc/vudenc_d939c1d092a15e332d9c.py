def get_result(self):...
self.cursor.execute('SELECT * FROM log_result WHERE campaign_id=?', [self.
    campaign['id']])
return self.cursor.fetchall()
