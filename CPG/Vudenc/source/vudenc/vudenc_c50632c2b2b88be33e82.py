def delete_cart(userId):...
sql_query = f"""
            DELETE FROM {CARTS_TABLE} 
            WHERE user_id={userId}
            """
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query)
connection.commit()
return 'Ok'
