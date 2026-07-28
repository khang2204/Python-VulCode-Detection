def update(self, table, dictionary=None):...
if table == 'campaign':
dictionary = self.campaign
if table == 'result':
if 'timestamp' in dictionary:
dictionary = self.result
dictionary['timestamp'] = datetime.now()
self.cursor.execute('UPDATE log_{} SET {}=? WHERE id={}'.format(table,
    '=?,'.join(dictionary.keys()), str(dictionary['id'])), list(dictionary.
    values()))
