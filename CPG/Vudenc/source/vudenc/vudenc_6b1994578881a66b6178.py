def get_product_reviews(productId, filters):...
offset = (filters['page'] - 1) * filters['perPage']
sql_query = f"""
            SELECT u.username, r.id, r.title, r.comment, r.rating, r.timestamp
            FROM {PRODUCTS_TABLE} p, {REVIEWS_TABLE} r, {USERS_TABLE} u
            WHERE p.id={productId} && r.user_id=u.id && r.product_id=p.id
            ORDER BY r.id DESC 
            LIMIT {offset}, {filters['perPage']}
            """
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query)
return cursor.fetchall()
