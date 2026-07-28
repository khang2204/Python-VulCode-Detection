def find_type_by_name(self, type_name):...
self.cursor.execute('SELECT * FROM product_type WHERE name = %s;', (type_name,)
    )
return self.cursor.fetchone()
