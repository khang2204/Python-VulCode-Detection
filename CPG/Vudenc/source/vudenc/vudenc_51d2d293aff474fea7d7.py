def get_count(self, item, item_from='result'):...
self.cursor.execute('SELECT COUNT(*) FROM log_' + item + ' WHERE ' +
    item_from + '_id=?', [getattr(self, item_from)['id']])
return self.cursor.fetchone()['COUNT(*)']
