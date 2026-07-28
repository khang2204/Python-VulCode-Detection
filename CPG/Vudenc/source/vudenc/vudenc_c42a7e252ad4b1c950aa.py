def get_id(self):...
conn = mysql.connection
cur = conn.cursor()
cur.execute('SELECT id FROM users WHERE username="%s" ' % self.username)
rv = cur.fetchall()
return str(rv[0]['id'])
