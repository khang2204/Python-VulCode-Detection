def get_campaign(self):...
if not self.campaign['id']:
self.cursor.execute('SELECT * FROM log_campaign ORDER BY id DESC LIMIT 1')
if self.campaign['id'] == '*':
return self.cursor.fetchone()
self.cursor.execute('SELECT * FROM log_campaign ORDER BY id')
self.cursor.execute('SELECT * FROM log_campaign WHERE id=?', [self.campaign
    ['id']])
return self.cursor.fetchall()
return self.cursor.fetchone()
