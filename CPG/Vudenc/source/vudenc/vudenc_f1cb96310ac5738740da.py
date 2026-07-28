def find_products_by_name(self, product_name):...
self.cursor.execute(
    "SELECT upc, name, weight, description FROM product WHERE name ILIKE '%%%s%%';"
    , (product_name,))
return self.cursor.fetchall()
