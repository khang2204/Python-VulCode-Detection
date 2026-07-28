def delete_product_from_cart(userId, productId):...
sql_query = f"""
            DELETE FROM {CARTS_TABLE} 
            WHERE user_id={userId} && product_id={productId}
            """
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query)
connection.commit()
return 'Ok'
