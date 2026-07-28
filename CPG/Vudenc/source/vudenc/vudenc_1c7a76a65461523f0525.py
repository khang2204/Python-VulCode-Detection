def get_total_departments_products(filters, department):...
sql_query = f"""
            SELECT COUNT(p.id) AS total
            FROM products AS p INNER JOIN {PRODUCTS_TYPES_TABLE} AS pt ON
            p.product_type_id=pt.id
            WHERE p.rating >= {filters['rating']}
            AND pt.name = '{department}'
            """
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query)
return int(cursor.fetchone()['total'])
