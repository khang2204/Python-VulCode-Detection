def create_junk_table(self):...
query = 'CREATE TABLE IF NOT EXISTS DPNET(why_mySQL int)'
self.cursor.execute(query)
self.connection.commit()
