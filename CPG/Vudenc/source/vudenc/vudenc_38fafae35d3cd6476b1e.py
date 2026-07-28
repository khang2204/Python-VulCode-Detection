def _purchase_by_product(self, product, quantity):...
"""docstring"""
product_id = product[0]
store_id = ONLINE_STORE_ID
customer_id = self.customer_id
self.cursor.execute(
    """
            SELECT product_id
            FROM store_sells_product
            WHERE product_id = %s
            AND store_id = %s;
            """
    , (product_id, store_id))
results = self.cursor.fetchall()
if len(results) == 0:
self.cursor.execute(
    """
            WITH current_purchase AS (
                INSERT INTO purchase (datetime, store_id, customer_id)
                VALUES (NOW(), %(store_id)s, %(customer_id)s)
                RETURNING id AS purchase_id
            )
            INSERT INTO product_in_purchase (product_id, purchase_id)
            VALUES (%(product_id)s, (SELECT purchase_id FROM current_purchase));
            """
    , {'store_id': store_id, 'customer_id': customer_id, 'product_id':
    product_id})
self.db_conn.commit()
