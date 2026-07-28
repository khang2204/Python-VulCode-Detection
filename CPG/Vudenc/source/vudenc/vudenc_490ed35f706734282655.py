def add_product_review(productId, userId, review):...
sql_query = f"""
            INSERT INTO {REVIEWS_TABLE} (user_id, product_id, title, comment, rating)
            VALUES({userId}, {productId}, '{review['title']}',
            '{review['comment']}', {review['rating']})
            """
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query)
connection.commit()
