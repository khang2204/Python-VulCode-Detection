def get_products(filters):...
offset = (filters['page'] - 1) * filters['perPage']
sql_query = f"""
            SELECT p.id, p.ean, p.name, p.description, pt.name AS type, p.company, p.price, p.rating, p.weight, p.quantity, p.image_url
            FROM {PRODUCTS_TABLE} AS p INNER JOIN {PRODUCTS_TYPES_TABLE} AS pt ON
            p.product_type_id=pt.id
            WHERE p.rating >= {filters['rating']}
            ORDER BY p.id LIMIT {offset}, {filters['perPage']}
            """
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query)
return cursor.fetchall()
