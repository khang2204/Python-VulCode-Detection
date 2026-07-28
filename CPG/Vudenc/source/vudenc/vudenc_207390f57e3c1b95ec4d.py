def get_item(self, item):...
self.cursor.execute('SELECT * FROM log_' + item + ' WHERE result_id=? ', [
    self.result['id']])
return self.cursor.fetchall()
