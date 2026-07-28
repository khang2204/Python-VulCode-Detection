def insert(self, table, dictionary=None):...
if dictionary is None:
if table == 'campaign':
if 'timestamp' in dictionary:
dictionary = self.campaign
if table == 'result':
dictionary['timestamp'] = datetime.now()
if 'id' in dictionary:
dictionary = self.result
self.cursor.execute('INSERT INTO log_{} ({}) VALUES ({})'.format(table, ','
    .join(dictionary.keys()), ','.join('?' * len(dictionary))), list(
    dictionary.values()))
dictionary['id'] = self.cursor.lastrowid
