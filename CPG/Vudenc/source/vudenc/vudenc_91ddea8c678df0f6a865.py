def query(self, query='True', columns='*'):...
self.cursor.execute(self.SQL_QUERY_JSON % (columns, self.name, query))
rows = [item for item in self.cursor.fetchall()]
return rows
