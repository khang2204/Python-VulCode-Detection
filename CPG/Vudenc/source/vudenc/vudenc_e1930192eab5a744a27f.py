def update_cart_quantity(userId, productId, quantity):...
sql_query = f"""
            UPDATE {CARTS_TABLE}
            SET quantity = {quantity}
            WHERE user_id = {userId} AND product_id = {productId};
            """
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query)
connection.commit()
return 'Ok'
