def get_departments():...
sql_query = f"""
            SELECT name
            FROM {PRODUCTS_TYPES_TABLE}
            """
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query)
return cursor.fetchall()
