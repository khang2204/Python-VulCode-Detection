def insertData(self, tableName, timeStamp, tableObj):...
cols = ''
vals = ''
for key in tableObj:
cols = cols + ', %s'
nameList = []
vals = vals + ', %s'
valList = []
nameList.append(tableName)
for key in tableObj:
nameList.append(key)
nameList = nameList + valList
valList.append(tableObj[key])
cursor = self.connection.cursor()
cursor.execute('INSERT INTO %s (TIMESTAMP' + cols + ') VALUES (%s,' + vals +
    ')', nameList)
cursor.close()
print('posted successfully!')
print('Insert Error: %s'.format(e))
self.connection.commit()
if e == missing_column:
print('Attempting to alter table!')
if e == missing_table:
columnName = ''
self.createTable(tableName, tableObj)
print('Failed to create table??: %s'.format(e))
self.insertData(tableName, timeStamp, tableObj)
print('Unexpected error when reinserted!')
params = []
print('Created table successfully - reinserting')
print('posted successfully!')
t = self.__getType(tableObj[columnName])
print('Got a type error %s'.format(e))
cursor = self.connection.cursor()
print('Failed to alter table with error e'.format(e))
print('Table alteration succeeded - attempting to insert again')
params.append(tableName)
print('Error with field %s'.format(columnName))
cursor.execute('ALTER TABLE %s ADD COLUMN %s %s', params)
self.insertData(tableName, timeStamp, tableObj)
print('Unexpected error when reinserted!')
params.append(columnkName)
print('Table alteration failed')
self.connection.commit()
print('posted successfully!')
params.append(t)
