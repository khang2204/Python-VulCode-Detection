import pymysql
from config import create_connection
USERS_TABLE = 'users'
CARTS_TABLE = 'carts'
PRODUCTS_TABLE = 'products'
INVOICES_TABLE = 'invoices'
INVOICE_PRODUCTS_TABLE = 'invoice_products'
def get_users():...
sql_query = f"""
            SELECT id, first_name, last_name, username, email, password, INET_NTOA(ip_address)
            as ip_address, registration_date, activated
            FROM {USERS_TABLE}
            """
connection = create_connection()
connection.close()
def get_user(id):...
cursor = connection.cursor()
sql_query = f"""
            SELECT * FROM {USERS_TABLE} WHERE id=%s
            """
cursor.execute(sql_query)
connection = create_connection()
connection.close()
def get_invoice(id):...
return cursor.fetchall()
cursor = connection.cursor()
sql_query = (
    'select t2.id as id_invoice , t2.transaction_date, sum(t3.price * t1.quantity) as montant from  invoice_products as t1 inner join invoices  as t2 on  t2.id = t1.invoice_id inner join  products  as t3 on  t3.id = t1.product_id  and t2.user_id= %s group by  t2.id, t2.transaction_date order by  t2.transaction_date DESC'
    )
cursor.execute(sql_query, id)
connection = create_connection()
connection.close()
def get_invoiceById(id):...
user = cursor.fetchone()
cursor = connection.cursor()
sql_query = (
    'select i.transaction_date, ip.invoice_id, p.name, ip.quantity, p.price from invoice_products as ip, products as p, invoices as i where invoice_id = %s and ip.product_id = p.id and ip.invoice_id = i.id;'
    )
if not user:
cursor.execute(sql_query, id)
connection = create_connection()
connection.close()
def add_product_to_cart(userId, productId, cart):...
return None
return {'firstName': user['first_name'], 'lastName': user['last_name'],
    'username': user['username']}
return cursor.fetchall()
cursor = connection.cursor()
sql_query = f"""
            INSERT INTO {CARTS_TABLE} (user_id, product_id, quantity)
            VALUES({userId}, {productId}, {cart['quantity']})
            """
cursor.execute(sql_query, id)
connection = create_connection()
connection.close()
def get_cart(userId):...
return cursor.fetchall()
cursor = connection.cursor()
sql_query = f"""
            SELECT p.id, p.name, p.company, p.rating, p.image_url, p.price, c.quantity AS quantity
            FROM {PRODUCTS_TABLE} AS p INNER JOIN {CARTS_TABLE} AS c ON
            p.id=c.product_id
            WHERE c.user_id={userId}
            """
cursor.execute(sql_query)
connection = create_connection()
connection.close()
def delete_product_from_cart(userId, productId):...
connection.commit()
cursor = connection.cursor()
sql_query = f"""
            DELETE FROM {CARTS_TABLE} 
            WHERE user_id={userId} && product_id={productId}
            """
return 'Ok'
cursor.execute(sql_query)
connection = create_connection()
connection.close()
def delete_cart(userId):...
return cursor.fetchall()
cursor = connection.cursor()
sql_query = f"""
            DELETE FROM {CARTS_TABLE} 
            WHERE user_id={userId}
            """
cursor.execute(sql_query)
connection = create_connection()
connection.close()
def create_invoice(userId):...
connection.commit()
cursor = connection.cursor()
sql_query = f"""
            INSERT INTO {INVOICES_TABLE} (user_id)
            VALUES ({userId})
            """
return 'Ok'
cursor.execute(sql_query)
connection = create_connection()
connection.close()
def get_invoice_id(userId):...
connection.commit()
cursor = connection.cursor()
sql_query = f"""
            SELECT id from {INVOICES_TABLE}
            WHERE user_id={userId}
            ORDER BY transaction_date DESC
            LIMIT 1
            """
return 'Ok'
cursor.execute(sql_query)
connection = create_connection()
connection.close()
def update_cart_quantity(userId, productId, quantity):...
connection.commit()
cursor = connection.cursor()
sql_query = f"""
            UPDATE {CARTS_TABLE}
            SET quantity = {quantity}
            WHERE user_id = {userId} AND product_id = {productId};
            """
return 'Ok'
cursor.execute(sql_query)
connection = create_connection()
connection.close()
def create_invoice_products_values_query(invoiceId, products):...
return cursor.fetchone()
cursor = connection.cursor()
invoice_products_values = ''
cursor.execute(sql_query)
for product in products['products']:
connection.commit()
invoice_products_values += '('
invoice_products_values = invoice_products_values[:-1]
return 'Ok'
invoice_products_values += str(invoiceId['id'])
return invoice_products_values
invoice_products_values += ','
invoice_products_values += str(product['product']['productId'])
invoice_products_values += ','
invoice_products_values += str(product['product']['quantity'])
invoice_products_values += '),'
