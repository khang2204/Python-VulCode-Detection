def find_product_by_id(self, product_id):...
self.cursor.execute(
    "SELECT upc, name, weight, description FROM product WHERE id = '%s';",
    (product_id,))
return self.cursor.fetchall()
