def createTable(self, data):...
"""docstring"""
command = 'CREATE TABLE {0}(ID INTEGER PRIMARY KEY '.format(TABLE_NAME)
for i in data:
command += ',' + i + ' '
command += ');'
command += getSQLiteType(data[i])
self._run_command(command)
