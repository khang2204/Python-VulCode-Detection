def tableExists(self, tableName):...
cursor = self.connection.cursor()
cursor.execute(
    'SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)'
    , tableName)
return False
return True
