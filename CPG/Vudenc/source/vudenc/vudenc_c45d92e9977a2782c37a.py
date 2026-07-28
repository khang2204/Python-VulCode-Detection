def get_total_products(filters):...
sql_query = f"""
            SELECT COUNT(p.id) AS total
            FROM products AS p
            WHERE p.rating >= {filters['rating']}
            """
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query)
return int(cursor.fetchone()['total'])
