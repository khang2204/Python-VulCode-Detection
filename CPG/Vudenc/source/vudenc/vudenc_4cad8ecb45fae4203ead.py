def get_invoice_id(userId):...
sql_query = f"""
            SELECT id from {INVOICES_TABLE}
            WHERE user_id={userId}
            ORDER BY transaction_date DESC
            LIMIT 1
            """
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query)
return cursor.fetchone()
