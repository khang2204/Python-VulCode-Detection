def find_products_by_upc(self, product_upc):...
self.cursor.execute(
    "SELECT upc, name, weight, description FROM product WHERE upc ILIKE '%%%s%%';"
    , (product_upc,))
return self.cursor.fetchall()
