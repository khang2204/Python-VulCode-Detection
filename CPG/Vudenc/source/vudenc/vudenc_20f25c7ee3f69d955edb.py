def get_total_searched_products(filters, search):...
sql_query = f"""
            SELECT COUNT(p.id) AS total
            FROM {PRODUCTS_TABLE} AS p INNER JOIN {PRODUCTS_TYPES_TABLE} AS pt ON
            p.product_type_id=pt.id
            WHERE p.rating >= {filters['rating']}
            AND p.name LIKE '%{search}%'
            """
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query)
return int(cursor.fetchone()['total'])
