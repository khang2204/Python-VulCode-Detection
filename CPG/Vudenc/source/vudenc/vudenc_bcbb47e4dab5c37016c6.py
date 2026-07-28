def flow_table(self, limit=10):...
db = self.db
self.schema.limit = limit
FLOWS = self.schema.flows()
cursor = db.cursor()
cursor.execute('USE testgoflow')
cursor.execute(FLOWS)
r = cursor.fetchall()
t = Table()
t = t.table_from_rows(r, self.schema.column_order)
return t
