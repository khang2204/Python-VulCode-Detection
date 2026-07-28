def find_product_by_type(self, product_type):...
self.cursor.execute(
    """
            SELECT *
            FROM product
            WHERE id IN (
                SELECT product_id
                FROM product_to_types
                WHERE product_type_id = %s
            )
            """
    , (product_type,))
return self.cursor.fetchall()
