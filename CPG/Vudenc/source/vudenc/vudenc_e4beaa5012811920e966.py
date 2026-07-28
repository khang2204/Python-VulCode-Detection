import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
def __init__(self, connection_address, connection_port, user_name, password,...
self.connection = mysql.connector.connect(host=connection_address, user=
    user_name, password=password, db=database)
self.cursor = self.connection.cursor(buffered=True)
def create_junk_table(self):...
query = 'CREATE TABLE IF NOT EXISTS DPNET(why_mySQL int)'
self.cursor.execute(query)
self.connection.commit()
def destroy_junk_table(self):...
query = 'DROP TABLE IF EXISTS DPNET'
self.cursor.execute(query)
self.connection.commit()
def verify_account(self, email, user_password):...
query = "SELECT Pass FROM user WHERE Email = '" + email + "'"
self.cursor.execute(query)
fetch = self.cursor.fetchone()
password = ' '.join(map(str, fetch))
return check_password_hash(password, user_password)
