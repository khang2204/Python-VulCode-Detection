def get_total_product_reviews(productId):...
sql_query = f"""
            SELECT COUNT(r.id) AS total
            FROM {REVIEWS_TABLE} AS r
            WHERE r.product_id={productId}
            """
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query)
return int(cursor.fetchone()['total'])
