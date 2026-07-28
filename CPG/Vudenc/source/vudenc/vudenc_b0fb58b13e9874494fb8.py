def destroy_junk_table(self):...
query = 'DROP TABLE IF EXISTS DPNET'
self.cursor.execute(query)
self.connection.commit()
