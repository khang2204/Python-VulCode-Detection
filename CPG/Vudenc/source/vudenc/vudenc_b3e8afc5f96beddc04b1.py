def create_invoice(userId):...
sql_query = f"""
            INSERT INTO {INVOICES_TABLE} (user_id)
            VALUES ({userId})
            """
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query)
connection.commit()
return 'Ok'
