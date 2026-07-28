import pymysql
from config import create_connection
PRODUCTS_TABLE = 'products'
PRODUCTS_TYPES_TABLE = 'product_types'
REVIEWS_TABLE = 'reviews'
USERS_TABLE = 'users'
def get_products(filters):...
offset = (filters['page'] - 1) * filters['perPage']
sql_query = f"""
            SELECT p.id, p.ean, p.name, p.description, pt.name AS type, p.company, p.price, p.rating, p.weight, p.quantity, p.image_url
            FROM {PRODUCTS_TABLE} AS p INNER JOIN {PRODUCTS_TYPES_TABLE} AS pt ON
            p.product_type_id=pt.id
            WHERE p.rating >= {filters['rating']}
            ORDER BY p.id LIMIT {offset}, {filters['perPage']}
            """
connection = create_connection()
connection.close()
def get_department_products(filters, department):...
cursor = connection.cursor()
offset = (filters['page'] - 1) * filters['perPage']
cursor.execute(sql_query)
sql_query = f"""
            SELECT p.id, p.ean, p.name, p.description, pt.name AS type, p.company, p.price, p.rating, p.weight, p.quantity, p.image_url
            FROM {PRODUCTS_TABLE} AS p INNER JOIN {PRODUCTS_TYPES_TABLE} AS pt ON
            p.product_type_id=pt.id
            WHERE p.rating >= {filters['rating']}
            AND pt.name = '{department}'
            ORDER BY p.id LIMIT {offset}, {filters['perPage']}
            """
return cursor.fetchall()
connection = create_connection()
connection.close()
def search_products(filters, search):...
cursor = connection.cursor()
offset = (filters['page'] - 1) * filters['perPage']
cursor.execute(sql_query)
sql_query = f"""
            SELECT p.id, p.ean, p.name, p.description, pt.name AS type, p.company, p.price, p.rating, p.weight, p.quantity, p.image_url
            FROM {PRODUCTS_TABLE} AS p INNER JOIN {PRODUCTS_TYPES_TABLE} AS pt ON
            p.product_type_id=pt.id
            WHERE p.rating >= {filters['rating']}
            AND p.name LIKE '%{search}%'
            ORDER BY p.id LIMIT {offset}, {filters['perPage']}
            """
return cursor.fetchall()
connection = create_connection()
connection.close()
def get_total_products(filters):...
cursor = connection.cursor()
sql_query = f"""
            SELECT COUNT(p.id) AS total
            FROM products AS p
            WHERE p.rating >= {filters['rating']}
            """
cursor.execute(sql_query)
connection = create_connection()
connection.close()
def get_total_departments_products(filters, department):...
return cursor.fetchall()
cursor = connection.cursor()
sql_query = f"""
            SELECT COUNT(p.id) AS total
            FROM products AS p INNER JOIN {PRODUCTS_TYPES_TABLE} AS pt ON
            p.product_type_id=pt.id
            WHERE p.rating >= {filters['rating']}
            AND pt.name = '{department}'
            """
cursor.execute(sql_query)
connection = create_connection()
connection.close()
def get_product(productId):...
return int(cursor.fetchone()['total'])
cursor = connection.cursor()
sql_query = f"""
            SELECT p.ean, p.name, p.description, pt.name AS type, p.company, p.price, p.rating, p.weight, p.quantity, p.image_url
            FROM {PRODUCTS_TABLE} AS p INNER JOIN {PRODUCTS_TYPES_TABLE} AS pt ON
            p.product_type_id=pt.id WHERE p.id={productId}
            """
cursor.execute(sql_query)
connection = create_connection()
connection.close()
def get_product_reviews(productId, filters):...
return int(cursor.fetchone()['total'])
cursor = connection.cursor()
offset = (filters['page'] - 1) * filters['perPage']
cursor.execute(sql_query)
sql_query = f"""
            SELECT u.username, r.id, r.title, r.comment, r.rating, r.timestamp
            FROM {PRODUCTS_TABLE} p, {REVIEWS_TABLE} r, {USERS_TABLE} u
            WHERE p.id={productId} && r.user_id=u.id && r.product_id=p.id
            ORDER BY r.id DESC 
            LIMIT {offset}, {filters['perPage']}
            """
return cursor.fetchone()
connection = create_connection()
connection.close()
def get_total_searched_products(filters, search):...
cursor = connection.cursor()
sql_query = f"""
            SELECT COUNT(p.id) AS total
            FROM {PRODUCTS_TABLE} AS p INNER JOIN {PRODUCTS_TYPES_TABLE} AS pt ON
            p.product_type_id=pt.id
            WHERE p.rating >= {filters['rating']}
            AND p.name LIKE '%{search}%'
            """
cursor.execute(sql_query)
connection = create_connection()
connection.close()
def get_total_product_reviews(productId):...
return cursor.fetchall()
cursor = connection.cursor()
sql_query = f"""
            SELECT COUNT(r.id) AS total
            FROM {REVIEWS_TABLE} AS r
            WHERE r.product_id={productId}
            """
cursor.execute(sql_query)
connection = create_connection()
connection.close()
def add_product_review(productId, userId, review):...
return int(cursor.fetchone()['total'])
cursor = connection.cursor()
sql_query = f"""
            INSERT INTO {REVIEWS_TABLE} (user_id, product_id, title, comment, rating)
            VALUES({userId}, {productId}, '{review['title']}',
            '{review['comment']}', {review['rating']})
            """
cursor.execute(sql_query)
connection = create_connection()
connection.close()
return int(cursor.fetchone()['total'])
cursor = connection.cursor()
cursor.execute(sql_query)
connection.commit()
