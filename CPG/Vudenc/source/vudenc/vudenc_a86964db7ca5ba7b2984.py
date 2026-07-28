"""
All queries and commands that the user makes in the retail application
"""
import psycopg2
ONLINE_STORE_ID = 1
def __init__(self, dbname, user, password, host, port=5432):...
self.db_conn = psycopg2.connect(host=host, dbname=dbname, user=user,
    password=password, port=port)
self.cursor = self.db_conn.cursor()
def commit(self):...
self.db_conn.commit()
def __del__(self):...
self.cursor.close()
self.db_conn.close()
def login(self, customer_id):...
self.customer_id = customer_id
def find_product_by_id(self, product_id):...
self.cursor.execute(
    "SELECT upc, name, weight, description FROM product WHERE id = '%s';",
    (product_id,))
return self.cursor.fetchall()
