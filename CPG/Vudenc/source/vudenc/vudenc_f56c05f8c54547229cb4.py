def createTable(self, tableName, tableObj):...
cols = ''
for key in tableObj:
cols = cols + ', %s %s'
nameList = []
nameList.append(tableName)
for key in tableObj:
cursor = self.connection.cursor()
t = self.__getType(tableObj[key])
print('Error with object %s at key %s with value %s'.format(tableObj, key,
    tableObj[key]))
cursor.execute('CREATE TABLE %s (TIMESTAMP TIMESTAMPTZ NOT NULL' + cols +
    ')', nameList)
print('CREATE TABLE Error: %s'.format(e))
self.connection.commit()
nameList.append(key)
print('Caught error %s'.format(e))
nameList.append(t)
