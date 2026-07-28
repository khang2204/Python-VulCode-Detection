def find_brand_by_name(self, brand_name):...
self.cursor.execute("SELECT * FROM brand WHERE name ILIKE '%" + brand_name +
    "%';")
return self.cursor.fetchall()
