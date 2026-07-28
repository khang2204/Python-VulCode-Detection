def find_customer(self, username):...
self.cursor.execute(
    "SELECT * FROM customer WHERE LOWER(username) = LOWER('" + username + "');"
    )
return self.cursor.fetchone()
