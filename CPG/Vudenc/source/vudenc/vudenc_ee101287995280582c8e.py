def find_products_by_desc(self, product_desc):...
self.cursor.execute(
    "SELECT upc, name, weight, description FROM product WHERE description ILIKE '%%%s%%';"
    , (product_desc,))
return self.cursor.fetchall()
