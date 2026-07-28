def fetch_product(self):...
conn = sql.connect(self.dbStr)
c = conn.cursor()
c.execute('SELECT * FROM {tn} WHERE {upc}={my_upc}'.format(tn=self.
    table_name, cn=self.column_2, upc=self.column_2, my_upc=self.some_upc))
result = c.fetchone()
return result
