def add_product_to_cart(userId, productId, cart):...
sql_query = f"""
            INSERT INTO {CARTS_TABLE} (user_id, product_id, quantity)
            VALUES({userId}, {productId}, {cart['quantity']})
            """
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query)
connection.commit()
return 'Ok'
