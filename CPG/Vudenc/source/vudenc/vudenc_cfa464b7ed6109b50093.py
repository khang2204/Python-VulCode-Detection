import psycopg2
def __init__(self, host, port, database, username, password):...
self.connection = psycopg2.connect(dbname=database, host=host, port=port,
    user=username, password=password)
"""
    Inserts data into an existing table. On failure due to not enough columns
    will automatically add columns to the table as necessary.
    Takes:
    tableName - string of the table being inserted into
    timeStamp - the timeStamp of the insertion
    tableObj - a dict of key/value pairs to insert
    """
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
"""
    A private function that maps a type in python to a type in postgres
    Supports Strings, bools, numbers and arrays

    Raises a typerror on failure
    """
print('posted successfully!')
print('Insert Error: %s'.format(e))
def __getType(self, value):...
self.connection.commit()
if e == missing_column:
t = type(value)
print('Attempting to alter table!')
if e == missing_table:
if t is str:
columnName = ''
self.createTable(tableName, tableObj)
print('Failed to create table??: %s'.format(e))
self.insertData(tableName, timeStamp, tableObj)
print('Unexpected error when reinserted!')
return 'TEXT'
if t is bool:
params = []
print('Created table successfully - reinserting')
print('posted successfully!')
return 'BOOLEAN'
if t is int:
t = self.__getType(tableObj[columnName])
print('Got a type error %s'.format(e))
cursor = self.connection.cursor()
print('Failed to alter table with error e'.format(e))
print('Table alteration succeeded - attempting to insert again')
return 'DOUBLE PRECISION'
if t is float:
params.append(tableName)
print('Error with field %s'.format(columnName))
cursor.execute('ALTER TABLE %s ADD COLUMN %s %s', params)
self.insertData(tableName, timeStamp, tableObj)
print('Unexpected error when reinserted!')
return 'DOUBLE PRECISION'
if t is list:
params.append(columnkName)
print('Table alteration failed')
self.connection.commit()
print('posted successfully!')
t2 = type(value[0])
"""
    Creates a timescaledb table with at least a timestamp field. Partitions table
    by time.
    Takes:
    tableName - string of the table being inserted into
    tableObj - a dict of key/value pairs to start the table with
    """
params.append(t)
if t2 is str:
def createTable(self, tableName, tableObj):...
return 'TEXT[]'
if t2 is bool:
cols = ''
return 'BOOLEAN[]'
if t2 is int:
for key in tableObj:
return 'DOUBLE PRECISION[]'
if t2 is float:
cols = cols + ', %s %s'
nameList = []
return 'DOUBLE PRECISION[]'
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
"""
    Checks if a table exists
    takes:
    tableName - name of the table
    """
nameList.append(t)
def tableExists(self, tableName):...
cursor = self.connection.cursor()
cursor.execute(
    'SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)'
    , tableName)
return False
return True
